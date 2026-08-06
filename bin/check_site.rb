#!/usr/bin/env ruby

require "nokogiri"
require "pathname"
require "uri"

root = Pathname(ARGV.fetch(0, "_site")).expand_path
site_origin = "https://aabbccdkg.com"
failures = []
document_cache = {}
stylesheet_paths = []

def inside_root?(path, root)
  path == root || path.to_s.start_with?("#{root}#{File::SEPARATOR}")
end

def candidates_for(path)
  [path, path.join("index.html")]
end

def local_reference(raw, base_path, root, site_origin)
  return if raw.nil? || raw.empty? || raw.start_with?("data:", "mailto:", "tel:", "javascript:")

  uri = URI.parse(raw)
  if uri.host
    site_uri = URI.parse(site_origin)
    same_origin = uri.scheme&.casecmp?(site_uri.scheme) && uri.host.casecmp?(site_uri.host) && uri.port == site_uri.port
    return unless same_origin
  end
  return if uri.host.nil? && raw.start_with?("//")
  return if uri.scheme && !%w[http https].include?(uri.scheme)

  decoded_path = URI::DEFAULT_PARSER.unescape(uri.path.to_s)
  target = if decoded_path.empty?
             base_path
           elsif decoded_path.start_with?("/")
             root.join(decoded_path.delete_prefix("/"))
           else
             base_path.dirname.join(decoded_path)
           end.cleanpath

  [target, uri.fragment]
rescue URI::InvalidURIError
  [:invalid_uri, nil]
end

html_files = Dir[root.join("**/*.html")].sort.map { |file| Pathname(file) }
abort("Generated-site validation failed: no HTML files found under #{root}") if html_files.empty?
html_files.each do |file|
  html = File.read(file)
  failures << "#{file.relative_path_from(root)}: unresolved template placeholder" if html.include?("{{version}}")
  document = Nokogiri::HTML(html)
  document_cache[file.expand_path.to_s] = document

  document.css("a[href], img[src], script[src], link[href]").each do |node|
    raw = node["href"] || node["src"]
    reference = local_reference(raw, file, root, site_origin)
    next unless reference

    target, fragment = reference
    if target == :invalid_uri
      failures << "#{file.relative_path_from(root)}: invalid URI: #{raw}"
      next
    end
    unless inside_root?(target, root)
      failures << "#{file.relative_path_from(root)}: path escapes site root: #{raw}"
      next
    end

    resolved = candidates_for(target).find(&:file?)
    unless resolved
      failures << "#{file.relative_path_from(root)}: missing local target: #{raw}"
      next
    end

    next if fragment.nil? || fragment.empty? || resolved.extname != ".html"

    target_document = document_cache[resolved.expand_path.to_s] ||= Nokogiri::HTML(File.read(resolved))
    decoded_fragment = URI::DEFAULT_PARSER.unescape(fragment)
    selector = "[id=#{decoded_fragment.inspect}], [name=#{decoded_fragment.inspect}]"
    failures << "#{file.relative_path_from(root)}: missing fragment target: #{raw}" unless target_document.at_css(selector)
  end

  document.css("link[rel~='stylesheet'][href]").each do |node|
    reference = local_reference(node["href"], file, root, site_origin)
    next unless reference

    target, = reference
    if target == :invalid_uri
      failures << "#{file.relative_path_from(root)}: invalid stylesheet URI: #{node["href"]}"
      next
    end
    stylesheet_paths << target if inside_root?(target, root) && target.file? && target.extname == ".css"
  end
end

stylesheet_paths.uniq.sort.each do |file|
  File.read(file).scan(/url\((['"]?)(.*?)\1\)/i).each do |_quote, raw|
    reference = local_reference(raw, file, root, site_origin)
    next unless reference

    target, = reference
    if target == :invalid_uri
      failures << "#{file.relative_path_from(root)}: invalid CSS URI: #{raw}"
    elsif !inside_root?(target, root)
      failures << "#{file.relative_path_from(root)}: CSS path escapes site root: #{raw}"
    elsif !target.file?
      failures << "#{file.relative_path_from(root)}: missing CSS asset: #{raw}"
    end
  end
end

abort("Generated-site validation failed:\n#{failures.uniq.join("\n")}") unless failures.empty?

puts "Generated-site validation passed: #{html_files.size} HTML files."
