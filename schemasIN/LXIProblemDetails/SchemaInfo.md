---
layout: default
title: LXI Problem Details Schema
nav_order:  1
parent: LXI API Schemas
---

# LXI Problem Details Schema

The LXI Problem Details schema provides detailed explanation from 
the device regarding HTTP operations that do not have an implicit 
response. Further detail could be an explanation of error 
conditions, or other device status regarding the invoked method.

If the HTTP response is OK (200), the LXIProblemDetails response is 
not required.


For some use cases, such as determining authentication requirements, 
it may be appropriate for a client to intentionally generate an HTTP 
error then use this structure and the response headers to determine 
the requirements to access the designated resource.

In such cases, the information in this element may be redundant with 
information also available from response headers.

