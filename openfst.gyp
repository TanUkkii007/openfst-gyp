{
  'variables': {
    'openfst_dir': 'openfst-1.5.3',
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
      'target_name': 'include',
      'type': 'static_library',
      'direct_dependent_settings': {
        'include_dirs': [
          '<(openfst_dir)/src/include',
        ],
      },
      'sources': [
        '<(openfst_dir)/src/include/fst/arc.h',
        '<(openfst_dir)/src/include/fst/determinize.h',
        '<(openfst_dir)/src/include/fst/intersect.h',
        '<(openfst_dir)/src/include/fst/queue.h',
        '<(openfst_dir)/src/include/fst/statesort.h',
        '<(openfst_dir)/src/include/fst/arcfilter.h',
        '<(openfst_dir)/src/include/fst/dfs-visit.h',
        '<(openfst_dir)/src/include/fst/invert.h',
        '<(openfst_dir)/src/include/fst/randequivalent.h',
        '<(openfst_dir)/src/include/fst/string-weight.h',
        '<(openfst_dir)/src/include/fst/difference.h',
        '<(openfst_dir)/src/include/fst/lexicographic-weight.h',
        '<(openfst_dir)/src/include/fst/randgen.h',
        '<(openfst_dir)/src/include/fst/symbol-table.h',
        '<(openfst_dir)/src/include/fst/arcsort.h',
        '<(openfst_dir)/src/include/fst/encode.h',
        '<(openfst_dir)/src/include/fst/lock.h',
        '<(openfst_dir)/src/include/fst/random-weight.h',
        '<(openfst_dir)/src/include/fst/synchronize.h',
        '<(openfst_dir)/src/include/fst/epsnormalize.h',
        '<(openfst_dir)/src/include/fst/log.h',
        '<(openfst_dir)/src/include/fst/rational.h',
        '<(openfst_dir)/src/include/fst/test-properties.h',
        '<(openfst_dir)/src/include/fst/cache.h',
        '<(openfst_dir)/src/include/fst/equal.h',
        '<(openfst_dir)/src/include/fst/arc-map.h',
        '<(openfst_dir)/src/include/fst/map.h',
        '<(openfst_dir)/src/include/fst/register.h',
        '<(openfst_dir)/src/include/fst/topsort.h',
        '<(openfst_dir)/src/include/fst/closure.h',
        '<(openfst_dir)/src/include/fst/equivalent.h',
        '<(openfst_dir)/src/include/fst/matcher.h',
        '<(openfst_dir)/src/include/fst/matcher-fst.h',
        '<(openfst_dir)/src/include/fst/relabel.h',
        '<(openfst_dir)/src/include/fst/union-find.h',
        '<(openfst_dir)/src/include/fst/compact-fst.h',
        '<(openfst_dir)/src/include/fst/expanded-fst.h',
        '<(openfst_dir)/src/include/fst/minimize.h',
        '<(openfst_dir)/src/include/fst/replace.h',
        '<(openfst_dir)/src/include/fst/union.h',
        '<(openfst_dir)/src/include/fst/compat.h',
        '<(openfst_dir)/src/include/fst/factor-weight.h',
        '<(openfst_dir)/src/include/fst/state-map.h',
        '<(openfst_dir)/src/include/fst/mutable-fst.h',
        '<(openfst_dir)/src/include/fst/reverse.h',
        '<(openfst_dir)/src/include/fst/util.h',
        '<(openfst_dir)/src/include/fst/complement.h',
        '<(openfst_dir)/src/include/fst/flags.h',
        '<(openfst_dir)/src/include/fst/partition.h',
        '<(openfst_dir)/src/include/fst/reweight.h',
        '<(openfst_dir)/src/include/fst/vector-fst.h',
        '<(openfst_dir)/src/include/fst/filter-state.h',
        '<(openfst_dir)/src/include/fst/compose-filter.h',
        '<(openfst_dir)/src/include/fst/float-weight.h',
        '<(openfst_dir)/src/include/fst/product-weight.h',
        '<(openfst_dir)/src/include/fst/rmepsilon.h',
        '<(openfst_dir)/src/include/fst/verify.h',
        '<(openfst_dir)/src/include/fst/compose.h',
        '<(openfst_dir)/src/include/fst/fst-decl.h',
        '<(openfst_dir)/src/include/fst/project.h',
        '<(openfst_dir)/src/include/fst/rmfinalepsilon.h',
        '<(openfst_dir)/src/include/fst/visit.h',
        '<(openfst_dir)/src/include/fst/concat.h',
        '<(openfst_dir)/src/include/fst/fst.h',
        '<(openfst_dir)/src/include/fst/properties.h',
        '<(openfst_dir)/src/include/fst/shortest-distance.h',
        '<(openfst_dir)/src/include/fst/weight.h',
        '<(openfst_dir)/src/include/fst/connect.h',
        '<(openfst_dir)/src/include/fst/fstlib.h',
        '<(openfst_dir)/src/include/fst/prune.h',
        '<(openfst_dir)/src/include/fst/shortest-path.h',
        '<(openfst_dir)/src/include/fst/const-fst.h',
        '<(openfst_dir)/src/include/fst/heap.h',
        '<(openfst_dir)/src/include/fst/push.h',
        '<(openfst_dir)/src/include/fst/state-table.h',
        '<(openfst_dir)/src/include/fst/pair-weight.h',
        '<(openfst_dir)/src/include/fst/config.h',
        '<(openfst_dir)/src/include/fst/tuple-weight.h',
        '<(openfst_dir)/src/include/fst/power-weight.h',
        '<(openfst_dir)/src/include/fst/lookahead-matcher.h',
        '<(openfst_dir)/src/include/fst/types.h',
        '<(openfst_dir)/src/include/fst/add-on.h',
        '<(openfst_dir)/src/include/fst/label-reachable.h',
        '<(openfst_dir)/src/include/fst/accumulator.h',
        '<(openfst_dir)/src/include/fst/interval-set.h',
        '<(openfst_dir)/src/include/fst/state-reachable.h',
        '<(openfst_dir)/src/include/fst/lookahead-filter.h',
        '<(openfst_dir)/src/include/fst/generic-register.h',
        '<(openfst_dir)/src/include/fst/edit-fst.h',
        '<(openfst_dir)/src/include/fst/replace-util.h',
        '<(openfst_dir)/src/include/fst/icu.h',
        '<(openfst_dir)/src/include/fst/string.h',
        '<(openfst_dir)/src/include/fst/signed-log-weight.h',
        '<(openfst_dir)/src/include/fst/sparse-tuple-weight.h',
        '<(openfst_dir)/src/include/fst/sparse-power-weight.h',
        '<(openfst_dir)/src/include/fst/expectation-weight.h',
        '<(openfst_dir)/src/include/fst/symbol-table-ops.h',
        '<(openfst_dir)/src/include/fst/bi-table.h',
        '<(openfst_dir)/src/include/fst/mapped-file.h',
        '<(openfst_dir)/src/include/fst/memory.h',
        '<(openfst_dir)/src/include/fst/filter-state.h',
        '<(openfst_dir)/src/include/fst/disambiguate.h',
        '<(openfst_dir)/src/include/fst/isomorphic.h',
        '<(openfst_dir)/src/include/fst/union-weight.h',
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
    {
      'target_name': 'fstngram',
      'product_name': 'libfstngram',
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
        '<(openfst_dir)/src/extensions/ngram/bitmap-index.cc',
        '<(openfst_dir)/src/extensions/ngram/ngram-fst.cc',
        '<(openfst_dir)/src/extensions/ngram/nthbit.cc',
      ],
    },
  ],
}
