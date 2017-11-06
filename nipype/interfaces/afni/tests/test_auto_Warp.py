# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from __future__ import unicode_literals
from ..preprocess import Warp


def test_Warp_inputs():
    input_map = dict(args=dict(argstr='%s',
    ),
    deoblique=dict(argstr='-deoblique',
    ),
    environ=dict(nohash=True,
    usedefault=True,
    ),
    gridset=dict(argstr='-gridset %s',
    ),
    ignore_exception=dict(nohash=True,
    usedefault=True,
    ),
    in_file=dict(argstr='%s',
    copyfile=False,
    mandatory=True,
    position=-1,
    ),
    interp=dict(argstr='-%s',
    ),
    matparent=dict(argstr='-matparent %s',
    ),
    mni2tta=dict(argstr='-mni2tta',
    ),
    newgrid=dict(argstr='-newgrid %f',
    ),
    num_threads=dict(nohash=True,
    usedefault=True,
    ),
    oblique_parent=dict(argstr='-oblique_parent %s',
    ),
    out_file=dict(argstr='-prefix %s',
    name_source='in_file',
    name_template='%s_warp',
    ),
    outputtype=dict(),
    terminal_output=dict(deprecated='1.0.0',
    nohash=True,
    ),
    tta2mni=dict(argstr='-tta2mni',
    ),
    verbose=dict(argstr='-verb',
    ),
    zpad=dict(argstr='-zpad %d',
    ),
    )
    inputs = Warp.input_spec()

    for key, metadata in list(input_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(inputs.traits()[key], metakey) == value


def test_Warp_outputs():
    output_map = dict(out_file=dict(),
    )
    outputs = Warp.output_spec()

    for key, metadata in list(output_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(outputs.traits()[key], metakey) == value
