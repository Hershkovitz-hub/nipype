# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from __future__ import unicode_literals
from ..epi import Eddy


def test_Eddy_inputs():
    input_map = dict(args=dict(argstr='%s',
    ),
    dont_peas=dict(argstr='--dont_peas',
    ),
    dont_sep_offs_move=dict(argstr='--dont_sep_offs_move',
    ),
    environ=dict(nohash=True,
    usedefault=True,
    ),
    fep=dict(argstr='--fep',
    ),
    field=dict(argstr='--field=%s',
    ),
    field_mat=dict(argstr='--field_mat=%s',
    ),
    flm=dict(argstr='--flm=%s',
    ),
    fudge_factor=dict(argstr='--ff=%s',
    ),
    fwhm=dict(argstr='--fwhm=%s',
    ),
    ignore_exception=dict(nohash=True,
    usedefault=True,
    ),
    in_acqp=dict(argstr='--acqp=%s',
    mandatory=True,
    ),
    in_bval=dict(argstr='--bvals=%s',
    mandatory=True,
    ),
    in_bvec=dict(argstr='--bvecs=%s',
    mandatory=True,
    ),
    in_file=dict(argstr='--imain=%s',
    mandatory=True,
    ),
    in_index=dict(argstr='--index=%s',
    mandatory=True,
    ),
    in_mask=dict(argstr='--mask=%s',
    mandatory=True,
    ),
    in_topup_fieldcoef=dict(argstr='--topup=%s',
    requires=['in_topup_movpar'],
    ),
    in_topup_movpar=dict(requires=['in_topup_fieldcoef'],
    ),
    interp=dict(argstr='--interp=%s',
    ),
    is_shelled=dict(argstr='--data_is_shelled',
    ),
    method=dict(argstr='--resamp=%s',
    ),
    niter=dict(argstr='--niter=%s',
    ),
    num_threads=dict(nohash=True,
    usedefault=True,
    ),
    nvoxhp=dict(argstr='--nvoxhp=%s',
    ),
    out_base=dict(argstr='--out=%s',
    usedefault=True,
    ),
    output_type=dict(),
    repol=dict(argstr='--repol',
    ),
    session=dict(argstr='--session=%s',
    ),
    slm=dict(argstr='--slm=%s',
    ),
    terminal_output=dict(deprecated='1.0.0',
    nohash=True,
    ),
    use_cuda=dict(),
    )
    inputs = Eddy.input_spec()

    for key, metadata in list(input_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(inputs.traits()[key], metakey) == value


def test_Eddy_outputs():
    output_map = dict(out_corrected=dict(),
    out_movement_rms=dict(),
    out_outlier_report=dict(),
    out_parameter=dict(),
    out_restricted_movement_rms=dict(),
    out_rotated_bvecs=dict(),
    out_shell_alignment_parameters=dict(),
    )
    outputs = Eddy.output_spec()

    for key, metadata in list(output_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(outputs.traits()[key], metakey) == value
