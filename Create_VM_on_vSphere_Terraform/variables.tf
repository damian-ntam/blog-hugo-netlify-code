
variable "vsphere_server" {
  type    = string
  default = "10.16.2.99"
}

variable "vsphere_user" {
  type    = string
  default = "administrator@vsphere.local"
}

variable "vsphere_password" {
  type    = string
  default = "---"
}

variable "vsphere_datacenter" {
  type    = string
  default = "SaS-DC"
}

variable "vsphere_datastore" {
  type    = string
  default = "datastore-UCS-POD1-2"
}


variable "vsphere_compute_cluster" {
  type    = string
  default = "SaS-Cluster"
}

variable "vsphere_template" {
  type    = string
  default = "ubuntu-1604-server-template"
}

variable "folder" {
  type    = string
  default = "wauterw"
}

variable "aci_vm1_name" {
  type    = string
  default = "ACI1-noACI"
}

variable "aci_vm2_name" {
  type    = string
  default = "ACI2-noACI"
}

variable "aci_vm1_address" {
  type    = string
  default = "10.16.2.233"
}

variable "aci_vm2_address" {
  type    = string
  default = "10.16.2.234"
}

variable "gateway" {
  type    = string
  default = "10.16.2.254"
}

variable "dns_list" {
  type    = string
  default = "10.9.15.1"
}

variable "dns_search" {
  type    = string
  default = "cisco.com"
}

variable "domain_name" {
  type    = string
  default = "cisco.com"
}
