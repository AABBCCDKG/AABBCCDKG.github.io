---
layout: post
title: 博士申请记录(2) 
date: 2024-09-04 00:32:13
description: 
tags: phd-application
categories: phd-application
tabs: true
---
我们有很多条路可以到达目标，但两点之间的直线最短。在这条直线上分布着需要解决的问题，这些问题符合二八定律。每次向经验丰富的人请教，都是在直线上解决一个小核心问题。

<div style="text-align: center;">
    （科研进度/和过来人的交流密度）
</div>

了解如何准备RA申请 -> 申请RA -> 拿Return Offer: **Nathan Zhang Meeting - 30 Mins**

修改Proposal -> 写代码 -> 写文章 -> 发文章

理解概念 -> 加入Ultima的项目 -> 发文章
















目标: 


草稿：

Question List:

    1. (Match) I noticed that Professor Kunle has recently published many papers on Dataflow, and I also found some of his earlier talks on the subject. Does this mean that Professor Kunle's current primary research focus is on how to use Dataflow Architecture to improve computing performance, especially for machine learning? Or could you provide an overview of the current focus of Professor's research group?

    2. (Connection) While I'm planning to apply for a PhD starting in 2026, I've decided to accelerate my degree process and aim to graduate in May next year so that I can apply for an on-site Research Assistant position. I'm very interested in the possibility of working with Professor Kunle. Given this, how would you suggest I plan my time between now and then? In the longer term, what qualities does Professor Kunle typically look for in his students? If you could provide some specific examples, that would be very helpful!! Additionally, what are the best ways to stay informed about the latest developments in his lab? Would Google Scholar be a good resource for this?






目标：

A (修改Proposal) -> 写代码 -> 写文章 -> 发文章

B 理解概念 -> 加入Ultima的项目 -> 发文章

核心问题：

A More general and practical 

B 




1. 目前只能识别简单图像，对于复杂图像，需要进行一些处理才能让 Hough-circle 等工具正确识别。

    预处理图像：首先可以通过灰度化、去噪、增强对比度等预处理步骤，减少图像中的噪声和不必要的细节，从而使得边缘检测等工具更容易识别出感兴趣的区域。

    应用高斯模糊：在图像上应用高斯模糊可以减少细小噪声的影响，使得边缘检测算法（如 Canny 边缘检测）在处理时更加稳定。

    边缘检测：使用 Canny 等边缘检测算法来识别图像中的边缘，然后将其输入到 Hough-circle 等工具中。这可以提高检测的准确性。

    形态学操作：可以使用形态学操作，如膨胀和腐蚀，以连接或分离图像中的边缘，从而更好地提取圆形特征。

    自适应阈值：使用自适应阈值方法对图像进行二值化处理，以更好地分离出圆形特征。

    多尺度检测：在不同的尺度上检测圆形特征，尤其是当图像中存在大小不同的圆时，使用多尺度检测可以帮助更准确地识别所有目标。

2. 识别复杂的不规则物体
    
    复杂的不规则物体可以看成简单物体的集合，用识别圆的工具识别一遍图片，勇矩形的工具再识别一遍，所有基础形状都过完之后，去掉内部线条，即为不规则物体

草稿
Ultima似乎和Chritofos的方向比较契合？都是cloud computing


在博士阶段，导师与学生的关系不再是传统意义上“传道授业解惑”的师生关系，而更像是后勤保障和前线部队。学生处在科研工作的最前线，负责实际的研究和探索，而导师的角色更倾向于为学生提供资源、指导方向和以及为学生闯的祸兜底。这意味优秀的博士候选人常常是先有了强烈的科研愿望，并且需要资源和支持来实现，才有了申请的博士的想法，并非是先申请博士，再进行科研。只有正确理解博士阶段导师和学生的关系，才能在科研上有所谓的“冲劲”。导师应该围绕学生的研究需求提供帮助，而不是学生被动地跟随导师。


<div style="text-align: center;">
    （动态）
</div>

目标：

A: Question List for Nathan Zhang

核心问题：了解Nathan + 了解什么可以提高自己申请到RA的概率

1. (Match)
I noticed that Professor Kunle has recently published many papers on Dataflow, and I also found some of his earlier talks on the subject. Does this mean that Professor Kunle's current primary research focus is on how to use Dataflow Architecture to improve computing performance, especially for machine learning? Or could you provide an overview of the current focus of Professor's research group?

2. (Connection)
While I'm planning to apply for a PhD starting in 2026, I've decided to accelerate my degree process and aim to graduate in May next year so that I can apply for an on-site Research Assistant position. I'm very interested in the possibility of working with Professor Kunle. Given this, how would you suggest I plan my time between now and then? In the longer term, what qualities does Professor Kunle typically look for in his students? If you could provide some specific examples, that would be very helpful!! Additionally, what are the best ways to stay informed about the latest developments in his lab? Would Google Scholar be a good resource for this?




