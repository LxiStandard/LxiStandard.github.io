---
layout: default
title: LXI Certificate Reference Schema
nav_order:  1
parent: Schemas
---

# LXI Certificate Reference Schema

The LXI Certificate Reference Schema indicates a single X.509
certificate, certificate chain, or CSR (Certificate Signing Request) 
that is on the device.

The certificate is not included in this schema, rather the entity on
the device is identified using a GUID. The GUID is assigned by the 
device and is returned by the Certificate List API.

The following examples are provided:

| Example | Purpose |
| ------------- |-------------|
| LXICertificateRefExample.xml | Simple example showing how to use the schema |
