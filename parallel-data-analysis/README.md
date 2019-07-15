# Data Analysis in Parallel
Speaker: [Filip Ter](https://github.com/terfilip/a)

## Description

This tutorial will demonstrate how to efficiently use IPyParallel, to benefit from parallelism in the early stages of data analysis and model development. The aim is to demystify parallelism for analysts and researchers, so that they can start using it early on in their workflow. Examples of common tasks will be shown in Jupyter, and how they can be easily run in parallel without major disruption.

## Abstract

Researchers, data scientists, and others; often encounter problems, which are parallel in nature. Despite this, many find it difficult to take advantage of the potential speedup afforded by parallelism, especially in the early stages of model development and data analysis. In such cases, one may write sequential code that only deals with a chunk of the data at a time, and then the parallelism is implemented once the code is moved into production. This approach is not ideal, as the original code written by the researcher will be slower, and may not map well onto the resulting production code. Thanks to technologies like IPyParallel it has become much easier to use parallelism in research, and this tutorial will demonstrate how that can be done.