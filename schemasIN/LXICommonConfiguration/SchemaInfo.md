---
layout: default
title: LXI Common Configuration Schema
nav_order:  1
parent: Schemas
---

# LXI Common Configuration Schema

The LXI Common Configuration XML schema is specified by the LXI 
Consortium as part of the LXI Security Extended Function.

LXICommonConfiguration contains settings related to the device 
secure configuration. This includes the configuration of the network 
interface, configuration of various network protocols and client 
authentication information.

This schema is used to:

  * Configure the security settings of a device
  * Interrogate a device to determine its security settings
  * Interrogate a device to determine its security capabilities

The following examples are provided:

| Example | Purpose |
| ------------- |-------------|
| LXICommonConfigurationExample.xml | Common Configuration Basic example with UnsecureMode as false |
| HashedPasswordExample.xml | Added a couple of passwords to the basic example  |
| LXICommonConfigurationExampleWithUnsecureModeEnabled.xml | Telnet and SCPIRaw enabled so UnsecureMode is enabled |

