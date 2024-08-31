---
layout: post
title: Top Research Labs in Machine Learning Systems (MLSys)🔬
date: 2024-05-01 00:32:13
description: A brief introduction to top-tier MLSys labs for Ph.D. applicants.
tags: MLSys-Learning-Journal
categories: MLSys-Learning-Journal
tabs: true
---
This is a brief introduction to top-tier MLSys labs for Ph.D. applicants, with a primary focus on those in the United States and mainland China. If there are any omissions, please feel free to [contact me](mailto:wangdong0502@gmail.com) to add them.
# United States

## [Google Brain](https://research.google/)

## [Microsoft Research (MSR)](https://www.microsoft.com/en-us/research/)
* [Fast and Efficient Infrastructure for Distributed Deep Learning (Fiddle)](https://www.microsoft.com/en-us/research/project/fiddle/)

## [Catalyst (Carnegie Mellon University)](https://catalyst.cs.cmu.edu/)
* [Eric Xing: ](https://www.cs.cmu.edu/~epxing/) Prof. Eric is a student of [Prof. Michael I. Jordan](https://people.eecs.berkeley.edu/~jordan/).

* [Tianqi Chen: ](https://tqchen.com/)

    * [TVM: ](https://tvm.apache.org/) TVM is an open-source framework for optimizing and deploying deep learning models, with its name derived from "Tensor Virtual Machine." Its primary goal is to optimize and compile deep learning models in an automated manner, enabling efficient execution on various hardware platforms such as CPUs, GPUs, FPGAs, and specialized AI accelerators.

    * [XGBoost: ](https://xgboost.readthedocs.io/en/stable/)XGBoost is an optimized distributed gradient boosting library designed to be highly efficient, flexible and portable. It implements machine learning algorithms under the Gradient Boosting framework. XGBoost provides a parallel tree boosting (also known as GBDT, GBM) that solve many data science problems in a fast and accurate way. The same code runs on major distributed environment (Hadoop, SGE, MPI) and can solve problems beyond billions of examples.

    * [MXNet: ](https://github.com/apache/mxnet)Apache MXNet is a deep learning framework designed for both efficiency and flexibility. It allows you to mix symbolic and imperative programming to maximize efficiency and productivity. At its core, MXNet contains a dynamic dependency scheduler that automatically parallelizes both symbolic and imperative operations on the fly. A graph optimization layer on top of that makes symbolic execution fast and memory efficient. MXNet is portable and lightweight, scalable to many GPUs and machines.

* [Zhihao Jia: ](https://www.cs.cmu.edu/~zhihaoj2/) Prof. Zhihao Jia is a student of [Prof. Matei Zaharia (now at UC Berkeley)](https://people.eecs.berkeley.edu/~matei/). He seems to be more focused on system for LLM.
    * [TASO: ](chrome-extension://efaidnbmnnnibpcajpcglclefindmkaj/https://cs.stanford.edu/~padon/taso-sosp19.pdf)
    * [Flexflow: ](https://flexflow.ai/)

## [DSAIL (MIT)](https://dsail.csail.mit.edu/)
* [Song Han: ](https://hanlab.mit.edu/songhan)Pruning and Sparse related work. Prof. Song Han seems to be working on algorithm modifications and hardware, and he's not really focused on TinyML anymore. Now he's working on diffusion models and LLM models.

* [Tim Kraska: ](https://people.csail.mit.edu/kraska/)


## [CSAIL (MIT)](https://www.csail.mit.edu/)
* [Tim Kraska: ](https://people.csail.mit.edu/kraska/) Learned Index

* [Saman Amarasinghe: ](https://www.csail.mit.edu/person/saman-amarasinghe)
    * [Halide](chrome-extension://efaidnbmnnnibpcajpcglclefindmkaj/https://people.csail.mit.edu/jrk/halide-pldi13.pdf)
    * [TACO](https://tacos.libraries.mit.edu/).

## [Stanford DAWN Project](https://dawn.cs.stanford.edu/)
* [Matei Zaharia (now at UC Berkeley): ](https://people.eecs.berkeley.edu/~matei/) Matei Zaharia (Stanford & Databricks) is highly respected for building [Apache Spark](https://spark.apache.org/) (one of the most widely used frameworks for distributed data processing, and co-started other datacenter software such as Apache Mesos and Spark Streaming) from scratch to a billion-dollar level. He serves as a PC and chair for major conferences. PipeDream, TASO, and FlexFlow is the project built by his Ph.D. student.Zhihao jia is his Ph.D. student. and  his students' projects like PipeDream, TASO by Zhihao Jia, and FlexFlow. One standout aspect of his research is that it addresses real system needs, making it impactful and practical. Not all his work prioritizes performance; for instance, one recent paper discusses offloading computation to GPUs using annotation for ease of use. Overall, pursuing a PhD under his guidance would likely lead to significant influence in the industry.

## [Hazy Research (Stanford AI Lab)](https://hazyresearch.stanford.edu/index)
This research group focuses on MLSys and also organized a seminar series called [Stanford MLSys Seminar Series](https://mlsys.stanford.edu/)

## [RISELab (University of California, Berkeley)](https://rise.cs.berkeley.edu/)
* [Ion Stoica: ](https://people.eecs.berkeley.edu/~istoica/) 

* [Michael Jordan: ](https://people.eecs.berkeley.edu/~jordan/)

Most recent project: [Ray](https://rise.cs.berkeley.edu/projects/ray/)

Professors at RISE Lab have offered a course called [AI for Systems and Systems for AI (CS294)](https://ucbrise.github.io/cs294-ai-sys-fa19/)

## [System Lab (University of Washington)](https://www.cs.washington.edu/research/systems)
* [Luis Ceze: ](https://homes.cs.washington.edu/~luisceze/) Prof. Luis Ceze focuses on Programming Language and Computer Architecture.
    * [TVM: ](https://tvm.apache.org/) TVM is an open-source framework for optimizing and deploying deep learning models, with its name derived from "Tensor Virtual Machine." Its primary goal is to optimize and compile deep learning models in an automated manner, enabling efficient execution on various hardware platforms such as CPUs, GPUs, FPGAs, and specialized AI accelerators

* [Arvind Krishnamurthy: ](https://www.cs.washington.edu/people/faculty/arvind) Prof. Arvind Krishnamurthy primarily focuses on computer networks. His work involves applying networking technology to address challenges in distributed machine learning. So there is always cutting-edge support in the field of networking.

## [Sample (University of Washington)](https://sampl.cs.washington.edu/)

## [SymbioticLab (University of Michigan, Ann Arbor)](https://symbioticlab.org/)
* [Mosharaf Chowdhury (the academic leader): ](https://www.mosharaf.com/) Prof. Mosharaf is a student of [Prof. Ion Stoica](https://people.eecs.berkeley.edu/~istoica/). He offers the course [Systems for AI (EECS598)](https://github.com/mosharaf/eecs598/tree/w21-ai)


## [System Group (New York University)](http://www.news.cs.nyu.edu/)
* [Jinyang Li: ](https://cims.nyu.edu/people/profiles/LI_Jinyang.html) She is the Ph.D. advisor of [Dr. Minjie Wang](https://jermainewang.github.io/)(the author of DGL)

## [Shivaram Venkataraman Research Group (University of Wisconsin, Madison)](https://shivaram.org/)
* [Shivaram Venkataraman: ](https://shivaram.org/) Prof. Shivaram is the student of [Prof. Ion Stoica](https://people.eecs.berkeley.edu/~istoica/). He understands more about machine learning and less about systems. The papers he published is not too many, but the workload is substantial.


## [EcoSystem (University of Toronto)](https://www.cs.toronto.edu/ecosystem/)
* [Gennady Pekhimenko: ](https://www.cs.toronto.edu/~pekhimenko/)


# China
In mainland China, it seems that most of the work in MLSys is being don in companies. However, some strong teams in distributed systems often also work on MLSys to some extent, such as [IPADS (Shanghai Jiaotong Univeristy).](https://ipads.se.sjtu.edu.cn/zh/index.html)

## [Microsoft Research Lab(Asia)](https://www.microsoft.com/en-us/research/group/systems-and-networking-research-group-asia/)

## [PACMAN Group(Tsinghua)](https://pacman.cs.tsinghua.edu.cn/)
More related to Arch

## [Center for Energy-efficient Computing and Applications(Peking University)](https://ceca.pku.edu.cn/people/index.htm)
More related to Arch

## [Cheng LI's Research Group (Univeristy of Science and Technology China)](http://staff.ustc.edu.cn/~chengli7)


## [IPADS(Shanghai Jiaotong Univeristy)](https://ipads.se.sjtu.edu.cn/zh/index.html)
The best System Lab in Mainland China, and now is also working on some MLSys projects.

# Appendix

## Some people worth following on Zhihu
* [Tianqi Chen: ](https://www.zhihu.com/people/crowowrk) Prof. Tianqi Chen is an Assistant Professor at Carnegie Mellon University. He helps run the [Catalyst Group](https://catalyst.cs.cmu.edu/).

* [Huaizheng Zhang: ](https://www.zhihu.com/people/zhanghuaizheng) Dr. Huaizheng Zhang's [AI-System-School](https://github.com/HuaizhengZhang/AI-System-School) is an open project aimed at collecting and organizing research papers, tools, and resources related to MLSys, Large Language Models (LLM), and Generative AI (GenAI). It provides researchers and engineers with a systematic learning path and practical guide to help them better understand and apply these cutting-edge technologies. Here is his [personal website](https://huaizheng.xyz/).

* [Yue Zhao: ](https://www.zhihu.com/people/breaknever) Prof. Yue Zhang is currently an Assistant Professor at the University of Southern California. He was also a student of Prof. Zhihao Jia. Here is his [personal website](https://github.com/yzhao062).