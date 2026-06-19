project('vfs_proprietary_libvfs_shim', 'c',
  version: '0.1',
  default_options: ['c_std=c11']
)

cc = meson.get_compiler('c')

# Dependencies
libfprint_dep = dependency('libfprint-2', required: true)
glib_dep = dependency('glib-2.0', version: '>=2.50')
gusb_dep = dependency('gusb', version: '>=0.3.0', required: true)

# Define paths clearly
src_dir = meson.current_source_dir()
vfs_lib_dir = src_dir / 'vendor' / 'lib'
vfs_lib_path = vfs_lib_dir / 'libvfsFprintWrapper.so'

# 1. Install the library
install_data(
  vfs_lib_path,
  install_dir: get_option('libdir')
)

# 2. Find the library for linking
libvfs = cc.find_library('vfsFprintWrapper', dirs: [vfs_lib_dir], required: true)

vfs_deps = [libfprint_dep, gusb_dep, glib_dep, libvfs]

# 3. Build the driver
vfs_sources = files(
  'vfs_proprietary/capture_helper.c',
  'vfs_proprietary/vfs_proprietary.c'
)

# Change this:
# vfs_proprietary_lib = static_library(...)

# To this:
vfs_proprietary_lib = shared_module('vfs_proprietary',
  vfs_sources,
  include_directories: include_directories('vfs_proprietary'),
  dependencies: vfs_deps,
  install: true,
  # This path is critical: fprintd looks here for dynamically loadable drivers
  install_dir: '/usr/lib/x86_64-linux-gnu/libfprint-2/drivers/'
)

meson.add_install_script('post_install.py')