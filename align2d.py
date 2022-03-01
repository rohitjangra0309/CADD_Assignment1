from modeller import *

env = Environ()
aln = Alignment(env)
mdl = Model(env, file='6zb4', model_segment=('FIRST:A','LAST:A'))
aln.append_model(mdl, align_codes='6zb4A', atom_files='6zb4.pdb')
aln.append(file='query.ali', align_codes='E484K')
aln.align2d(max_gap_length=50)
aln.write(file='queryResult.ali', alignment_format='PIR')
aln.write(file='queryResult.pap', alignment_format='PAP')
