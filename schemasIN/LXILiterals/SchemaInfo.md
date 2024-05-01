---
layout: default
title: LXI Literals Schema
nav_order:  1
parent: Schemas
---

# LXI Literals Schema

The LXI Literals schema contains a single element with optional 
arbitrary attributes. It is used to pass arbitrary data to a method. 
As such, it does not provide syntactic validation of parameters.

This schema is intended to be used by methods that require minimal 
parameters, and would derive very little benefit from schema-based 
syntactic validation.

Methods that utilize this schema must document the attribute names 
and types used.

The following examples are provided:

| Example | Purpose |
| ------------- |-------------|
| LXILiteralsExample.xml | Simple example showing how to use the schema |
