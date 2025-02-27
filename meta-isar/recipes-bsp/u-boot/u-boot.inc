# ---------------------------------------------------------------------------
# This Isar layer is part of MTDA
# Copyright (C) 2022 Siemens Digital Industries Software
# ---------------------------------------------------------------------------
# SPDX-License-Identifier: MIT
# ---------------------------------------------------------------------------

require recipes-bsp/u-boot/u-boot-custom.inc

# u-boot tools need OpenSSL headers/libraries
DEBIAN_BUILD_DEPENDS_append = ",libssl-dev:native,libssl-dev"

# Python packages needed during the build
DEBIAN_BUILD_DEPENDS_append = ",python3-distutils,python3-pkg-resources,python3-all-dev:native,swig"

dpkg_runbuild_prepend() {
    sed -i -e 's,U_BOOT_BIN,U_BOOT_TARGET,g' ${S}/debian/rules
}
