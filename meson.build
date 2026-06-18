project('vfs_proprietary_libvfs_shim', 'c',
  version: '0.1',
  default_options: ['c_std=c11']
)

cc = meson.get_compiler('c')

# 1. Define Dependencies FIRST
# Define system dependencies
libfprint_dep = dependency('libfprint-2', required: true)
glib_dep = dependency('glib-2.0', version: '>=2.50')
gusb_dep = dependency('gusb', version: '>=0.3.0', required: true)

# Define local vendor library
vendor_lib_dir = meson.current_source_dir() + '/vendor/lib'
libvfs = cc.find_library('vfsFprintWrapper', dirs: [vendor_lib_dir], required: true)

# Now create the array safely
vfs_deps = [libfprint_dep, gusb_dep, glib_dep, libvfs]

# 2. Define Sources
vfs_sources = files(
  'vfs_proprietary/capture_helper.c',
  'vfs_proprietary/vfs_proprietary.c'
)

# 3. Build
vfs_proprietary_lib = static_library('vfs_proprietary',
  vfs_sources,
  include_directories: include_directories('vfs_proprietary'),
  dependencies: vfs_deps, # Use the array here
  install: true
)