Jekyll::Hooks.register :site, :after_init do |site|
  libraries = site.config.fetch("third_party_libraries", {})

  libraries.each_value do |library|
    next unless library.is_a?(Hash) && library["version"] && library["url"]

    replace_version = lambda do |value|
      case value
      when Hash
        value.transform_values! { |nested_value| replace_version.call(nested_value) }
      when String
        value.gsub("{{version}}", library["version"].to_s)
      else
        value
      end
    end

    replace_version.call(library["url"])
  end
end
