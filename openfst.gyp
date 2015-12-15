{
  'variables': {
    'openfst_dir': 'openfst-1.5.0',
  },
  'target_defaults': {
    'cxxflags':[
      "-std=c++11",
    ],
    'xcode_settings': {
      'CLANG_CXX_LANGUAGE_STANDARD': 'c++11',
      'MACOSX_DEPLOYMENT_TARGET': '10.8',
      'CLANG_CXX_LIBRARY': 'libc++',
    },
  },
  'targets': [
    {
      'target_name': 'fstarcsort',
      'type': 'executable',
      'dependencies': [
        'lib',
        'script',
      ],
      'include_dirs': [
        '<(openfst_dir)/src/include',
      ],
      'sources': [
        '<(openfst_dir)/src/bin/fstarcsort.cc',
      ],
    },
    {
      'target_name': 'fstclosure',
      'type': 'executable',
      'dependencies': [
        'lib',
        'script',
      ],
      'include_dirs': [
        '<(openfst_dir)/src/include',
      ],
      'sources': [
        '<(openfst_dir)/src/bin/fstclosure.cc',
      ],
    },
    {
      'target_name': 'fstcompile',
      'type': 'executable',
      'dependencies': [
        'lib',
        'script',
      ],
      'include_dirs': [
        '<(openfst_dir)/src/include',
      ],
      'sources': [
        '<(openfst_dir)/src/bin/fstcompile.cc',
      ],
    },
    {
      'target_name': 'fstcompose',
      'type': 'executable',
      'dependencies': [
        'lib',
        'script',
      ],
      'include_dirs': [
        '<(openfst_dir)/src/include',
      ],
      'sources': [
        '<(openfst_dir)/src/bin/fstcompose.cc',
      ],
    },
    {
      'target_name': 'fstconcat',
      'type': 'executable',
      'dependencies': [
        'lib',
        'script',
      ],
      'include_dirs': [
        '<(openfst_dir)/src/include',
      ],
      'sources': [
        '<(openfst_dir)/src/bin/fstconcat.cc',
      ],
    },
    {
      'target_name': 'fstconnect',
      'type': 'executable',
      'dependencies': [
        'lib',
        'script',
      ],
      'include_dirs': [
        '<(openfst_dir)/src/include',
      ],
      'sources': [
        '<(openfst_dir)/src/bin/fstconnect.cc',
      ],
    },
    {
      'target_name': 'fstconvert',
      'type': 'executable',
      'dependencies': [
        'lib',
        'script',
      ],
      'include_dirs': [
        '<(openfst_dir)/src/include',
      ],
      'sources': [
        '<(openfst_dir)/src/bin/fstconvert.cc',
      ],
    },
    {
      'target_name': 'fstdeterminize',
      'type': 'executable',
      'dependencies': [
        'lib',
        'script',
      ],
      'include_dirs': [
        '<(openfst_dir)/src/include',
      ],
      'sources': [
        '<(openfst_dir)/src/bin/fstdeterminize.cc',
      ],
    },
    {
      'target_name': 'fstdifference',
      'type': 'executable',
      'dependencies': [
        'lib',
        'script',
      ],
      'include_dirs': [
        '<(openfst_dir)/src/include',
      ],
      'sources': [
        '<(openfst_dir)/src/bin/fstdifference.cc',
      ],
    },
    {
      'target_name': 'fstdisambiguate',
      'type': 'executable',
      'dependencies': [
        'lib',
        'script',
      ],
      'include_dirs': [
        '<(openfst_dir)/src/include',
      ],
      'sources': [
        '<(openfst_dir)/src/bin/fstdisambiguate.cc',
      ],
    },
    {
      'target_name': 'fstdraw',
      'type': 'executable',
      'dependencies': [
        'lib',
        'script',
      ],
      'include_dirs': [
        '<(openfst_dir)/src/include',
      ],
      'sources': [
        '<(openfst_dir)/src/bin/fstdraw.cc',
      ],
    },
    {
      'target_name': 'fstencode',
      'type': 'executable',
      'dependencies': [
        'lib',
        'script',
      ],
      'include_dirs': [
        '<(openfst_dir)/src/include',
      ],
      'sources': [
        '<(openfst_dir)/src/bin/fstencode.cc',
      ],
    },
    {
      'target_name': 'fstepsnormalize',
      'type': 'executable',
      'dependencies': [
        'lib',
        'script',
      ],
      'include_dirs': [
        '<(openfst_dir)/src/include',
      ],
      'sources': [
        '<(openfst_dir)/src/bin/fstepsnormalize.cc',
      ],
    },
    {
      'target_name': 'fstequal',
      'type': 'executable',
      'dependencies': [
        'lib',
        'script',
      ],
      'include_dirs': [
        '<(openfst_dir)/src/include',
      ],
      'sources': [
        '<(openfst_dir)/src/bin/fstequal.cc',
      ],
    },
    {
      'target_name': 'fstequivalent',
      'type': 'executable',
      'dependencies': [
        'lib',
        'script',
      ],
      'include_dirs': [
        '<(openfst_dir)/src/include',
      ],
      'sources': [
        '<(openfst_dir)/src/bin/fstequivalent.cc',
      ],
    },
    {
      'target_name': 'fstinfo',
      'type': 'executable',
      'dependencies': [
        'lib',
        'script',
      ],
      'include_dirs': [
        '<(openfst_dir)/src/include',
      ],
      'sources': [
        '<(openfst_dir)/src/bin/fstinfo.cc',
      ],
    },
    {
      'target_name': 'fstintersect',
      'type': 'executable',
      'dependencies': [
        'lib',
        'script',
      ],
      'include_dirs': [
        '<(openfst_dir)/src/include',
      ],
      'sources': [
        '<(openfst_dir)/src/bin/fstintersect.cc',
      ],
    },
    {
      'target_name': 'fstinvert',
      'type': 'executable',
      'dependencies': [
        'lib',
        'script',
      ],
      'include_dirs': [
        '<(openfst_dir)/src/include',
      ],
      'sources': [
        '<(openfst_dir)/src/bin/fstinvert.cc',
      ],
    },
    {
      'target_name': 'fstisomorphic',
      'type': 'executable',
      'dependencies': [
        'lib',
        'script',
      ],
      'include_dirs': [
        '<(openfst_dir)/src/include',
      ],
      'sources': [
        '<(openfst_dir)/src/bin/fstisomorphic.cc',
      ],
    },
    {
      'target_name': 'fstmap',
      'type': 'executable',
      'dependencies': [
        'lib',
        'script',
      ],
      'include_dirs': [
        '<(openfst_dir)/src/include',
      ],
      'sources': [
        '<(openfst_dir)/src/bin/fstmap.cc',
      ],
    },
    {
      'target_name': 'fstminimize',
      'type': 'executable',
      'dependencies': [
        'lib',
        'script',
      ],
      'include_dirs': [
        '<(openfst_dir)/src/include',
      ],
      'sources': [
        '<(openfst_dir)/src/bin/fstminimize.cc',
      ],
    },
    {
      'target_name': 'fstprint',
      'type': 'executable',
      'dependencies': [
        'lib',
        'script',
      ],
      'include_dirs': [
        '<(openfst_dir)/src/include',
      ],
      'sources': [
        '<(openfst_dir)/src/bin/fstprint.cc',
      ],
    },
    {
      'target_name': 'fstproject',
      'type': 'executable',
      'dependencies': [
        'lib',
        'script',
      ],
      'include_dirs': [
        '<(openfst_dir)/src/include',
      ],
      'sources': [
        '<(openfst_dir)/src/bin/fstproject.cc',
      ],
    },
    {
      'target_name': 'fstprune',
      'type': 'executable',
      'dependencies': [
        'lib',
        'script',
      ],
      'include_dirs': [
        '<(openfst_dir)/src/include',
      ],
      'sources': [
        '<(openfst_dir)/src/bin/fstprune.cc',
      ],
    },
    {
      'target_name': 'fstpush',
      'type': 'executable',
      'dependencies': [
        'lib',
        'script',
      ],
      'include_dirs': [
        '<(openfst_dir)/src/include',
      ],
      'sources': [
        '<(openfst_dir)/src/bin/fstpush.cc',
      ],
    },
    {
      'target_name': 'fstrandgen',
      'type': 'executable',
      'dependencies': [
        'lib',
        'script',
      ],
      'include_dirs': [
        '<(openfst_dir)/src/include',
      ],
      'sources': [
        '<(openfst_dir)/src/bin/fstrandgen.cc',
      ],
    },
    {
      'target_name': 'lib',
      'product_name': 'libfst',
      'type': 'static_library',
      'direct_dependent_settings': {
        'include_dirs': [
          '<(openfst_dir)/src/include',
        ],
      },
      'include_dirs': [
        '<(openfst_dir)/src/include',
      ],
      'sources': [
        '<(openfst_dir)/src/lib/compat.cc',
        '<(openfst_dir)/src/lib/flags.cc',
        '<(openfst_dir)/src/lib/fst.cc',
        '<(openfst_dir)/src/lib/mapped-file.cc',
        '<(openfst_dir)/src/lib/properties.cc',
        '<(openfst_dir)/src/lib/symbol-table-ops.cc',
        '<(openfst_dir)/src/lib/symbol-table.cc',
        '<(openfst_dir)/src/lib/util.cc',
      ],
    },
    {
      'target_name': 'script',
      'product_name': 'libfstscript',
      'type': 'static_library',
      'direct_dependent_settings': {
        'include_dirs': [
          '<(openfst_dir)/src/include',
        ],
      },
      'include_dirs': [
        '<(openfst_dir)/src/include',
      ],
      'sources': [
        '<(openfst_dir)/src/script/arcsort.cc',
        '<(openfst_dir)/src/script/closure.cc',
        '<(openfst_dir)/src/script/compile.cc',
        '<(openfst_dir)/src/script/compose.cc',
        '<(openfst_dir)/src/script/concat.cc',
        '<(openfst_dir)/src/script/connect.cc',
        '<(openfst_dir)/src/script/convert.cc',
        '<(openfst_dir)/src/script/decode.cc',
        '<(openfst_dir)/src/script/determinize.cc',
        '<(openfst_dir)/src/script/difference.cc',
        '<(openfst_dir)/src/script/disambiguate.cc',
        '<(openfst_dir)/src/script/draw.cc',
        '<(openfst_dir)/src/script/encode.cc',
        '<(openfst_dir)/src/script/epsnormalize.cc',
        '<(openfst_dir)/src/script/equal.cc',
        '<(openfst_dir)/src/script/equivalent.cc',
        '<(openfst_dir)/src/script/fst-class.cc',
        '<(openfst_dir)/src/script/info.cc',
        '<(openfst_dir)/src/script/intersect.cc',
        '<(openfst_dir)/src/script/invert.cc',
        '<(openfst_dir)/src/script/isomorphic.cc',
        '<(openfst_dir)/src/script/map.cc',
        '<(openfst_dir)/src/script/minimize.cc',
        '<(openfst_dir)/src/script/print.cc',
        '<(openfst_dir)/src/script/project.cc',
        '<(openfst_dir)/src/script/prune.cc',
        '<(openfst_dir)/src/script/push.cc',
        '<(openfst_dir)/src/script/randequivalent.cc',
        '<(openfst_dir)/src/script/randgen.cc',
        '<(openfst_dir)/src/script/relabel.cc',
        '<(openfst_dir)/src/script/replace.cc',
        '<(openfst_dir)/src/script/reverse.cc',
        '<(openfst_dir)/src/script/reweight.cc',
        '<(openfst_dir)/src/script/rmepsilon.cc',
        '<(openfst_dir)/src/script/script-impl.cc',
        '<(openfst_dir)/src/script/shortest-distance.cc',
        '<(openfst_dir)/src/script/shortest-path.cc',
        '<(openfst_dir)/src/script/synchronize.cc',
        '<(openfst_dir)/src/script/text-io.cc',
        '<(openfst_dir)/src/script/topsort.cc',
        '<(openfst_dir)/src/script/union.cc',
        '<(openfst_dir)/src/script/verify.cc',
        '<(openfst_dir)/src/script/weight-class.cc',
      ],
    },
    {
      'target_name': 'fst_test',
      'type': 'executable',
      'dependencies': [
        'lib',
      ],
      'direct_dependent_settings': {
        'include_dirs': [
          '<(openfst_dir)/src/include',
        ],
      },
      'include_dirs': [
        '<(openfst_dir)/src/include',
      ],
      'sources': [
        '<(openfst_dir)/src/test/fst_test.cc',
        '<(openfst_dir)/src/test/fst_test.h',
      ],
    },
    {
      'target_name': 'weight_test',
      'type': 'executable',
      'dependencies': [
        'lib',
      ],
      'direct_dependent_settings': {
        'include_dirs': [
          '<(openfst_dir)/src/include',
        ],
      },
      'include_dirs': [
        '<(openfst_dir)/src/include',
      ],
      'sources': [
        '<(openfst_dir)/src/test/weight_test.cc',
        '<(openfst_dir)/src/test/weight-tester.h',
      ],
    },
    {
      'target_name': 'algo_test',
      'type': 'executable',
      'dependencies': [
        'lib',
      ],
      'direct_dependent_settings': {
        'include_dirs': [
          '<(openfst_dir)/src/include',
        ],
      },
      'include_dirs': [
        '<(openfst_dir)/src/include',
      ],
      'sources': [
        '<(openfst_dir)/src/test/algo_test.cc',
        '<(openfst_dir)/src/test/algo_test.h',
      ],
    },
  ],
}
