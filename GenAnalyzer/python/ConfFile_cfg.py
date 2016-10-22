import FWCore.ParameterSet.Config as cms

process = cms.Process("Demo")

process.load("FWCore.MessageService.MessageLogger_cfi")
process.MessageLogger.cerr.FwkReport.reportEvery = 1

# Options and Output Report
process.options = cms.untracked.PSet(
	wantSummary = cms.untracked.bool(True)
)

process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(1000) )



process.source = cms.Source("PoolSource",
    # replace 'myfile.root' with the source file you want to use
    fileNames = cms.untracked.vstring(
	#'file:/afs/cern.ch/user/r/rasharma/work/aQGC_Studies/MC_SampleGeneration/analyzeLHE/CMSSW_8_0_11/src/GenAnalyzer_Arun/genAnalyzer/test/SMP-RunIISummer15wmLHEGS-00029_142.root'
	'file:/eos/uscms/store/user/rasharma/WlvWjjVBF2jets_EWK_LO_PythiaDecay/RunIISummer15wmLHEGS/161010_152335/0000/SMP-RunIISummer15wmLHEGS-00029_100.root',
	'file:/eos/uscms/store/user/rasharma/WlvWjjVBF2jets_EWK_LO_PythiaDecay/RunIISummer15wmLHEGS/161010_152335/0000/SMP-RunIISummer15wmLHEGS-00029_101.root',
	'file:/eos/uscms/store/user/rasharma/WlvWjjVBF2jets_EWK_LO_PythiaDecay/RunIISummer15wmLHEGS/161010_152335/0000/SMP-RunIISummer15wmLHEGS-00029_102.root',
	'file:/eos/uscms/store/user/rasharma/WlvWjjVBF2jets_EWK_LO_PythiaDecay/RunIISummer15wmLHEGS/161010_152335/0000/SMP-RunIISummer15wmLHEGS-00029_103.root',
	'file:/eos/uscms/store/user/rasharma/WlvWjjVBF2jets_EWK_LO_PythiaDecay/RunIISummer15wmLHEGS/161010_152335/0000/SMP-RunIISummer15wmLHEGS-00029_104.root',
	'file:/eos/uscms/store/user/rasharma/WlvWjjVBF2jets_EWK_LO_PythiaDecay/RunIISummer15wmLHEGS/161010_152335/0000/SMP-RunIISummer15wmLHEGS-00029_105.root',
	'file:/eos/uscms/store/user/rasharma/WlvWjjVBF2jets_EWK_LO_PythiaDecay/RunIISummer15wmLHEGS/161010_152335/0000/SMP-RunIISummer15wmLHEGS-00029_106.root',
	'file:/eos/uscms/store/user/rasharma/WlvWjjVBF2jets_EWK_LO_PythiaDecay/RunIISummer15wmLHEGS/161010_152335/0000/SMP-RunIISummer15wmLHEGS-00029_107.root',
	'file:/eos/uscms/store/user/rasharma/WlvWjjVBF2jets_EWK_LO_PythiaDecay/RunIISummer15wmLHEGS/161010_152335/0000/SMP-RunIISummer15wmLHEGS-00029_108.root',
	'file:/eos/uscms/store/user/rasharma/WlvWjjVBF2jets_EWK_LO_PythiaDecay/RunIISummer15wmLHEGS/161010_152335/0000/SMP-RunIISummer15wmLHEGS-00029_109.root',
	'file:/eos/uscms/store/user/rasharma/WlvWjjVBF2jets_EWK_LO_PythiaDecay/RunIISummer15wmLHEGS/161010_152335/0000/SMP-RunIISummer15wmLHEGS-00029_10.root',
	'file:/eos/uscms/store/user/rasharma/WlvWjjVBF2jets_EWK_LO_PythiaDecay/RunIISummer15wmLHEGS/161010_152335/0000/SMP-RunIISummer15wmLHEGS-00029_110.root',
	'file:/eos/uscms/store/user/rasharma/WlvWjjVBF2jets_EWK_LO_PythiaDecay/RunIISummer15wmLHEGS/161010_152335/0000/SMP-RunIISummer15wmLHEGS-00029_111.root',
	'file:/eos/uscms/store/user/rasharma/WlvWjjVBF2jets_EWK_LO_PythiaDecay/RunIISummer15wmLHEGS/161010_152335/0000/SMP-RunIISummer15wmLHEGS-00029_112.root',
	'file:/eos/uscms/store/user/rasharma/WlvWjjVBF2jets_EWK_LO_PythiaDecay/RunIISummer15wmLHEGS/161010_152335/0000/SMP-RunIISummer15wmLHEGS-00029_113.root',
	'file:/eos/uscms/store/user/rasharma/WlvWjjVBF2jets_EWK_LO_PythiaDecay/RunIISummer15wmLHEGS/161010_152335/0000/SMP-RunIISummer15wmLHEGS-00029_114.root',
	'file:/eos/uscms/store/user/rasharma/WlvWjjVBF2jets_EWK_LO_PythiaDecay/RunIISummer15wmLHEGS/161010_152335/0000/SMP-RunIISummer15wmLHEGS-00029_115.root',
	'file:/eos/uscms/store/user/rasharma/WlvWjjVBF2jets_EWK_LO_PythiaDecay/RunIISummer15wmLHEGS/161010_152335/0000/SMP-RunIISummer15wmLHEGS-00029_116.root',
	'file:/eos/uscms/store/user/rasharma/WlvWjjVBF2jets_EWK_LO_PythiaDecay/RunIISummer15wmLHEGS/161010_152335/0000/SMP-RunIISummer15wmLHEGS-00029_117.root',
	'file:/eos/uscms/store/user/rasharma/WlvWjjVBF2jets_EWK_LO_PythiaDecay/RunIISummer15wmLHEGS/161010_152335/0000/SMP-RunIISummer15wmLHEGS-00029_118.root',
	'file:/eos/uscms/store/user/rasharma/WlvWjjVBF2jets_EWK_LO_PythiaDecay/RunIISummer15wmLHEGS/161010_152335/0000/SMP-RunIISummer15wmLHEGS-00029_11.root',
	'file:/eos/uscms/store/user/rasharma/WlvWjjVBF2jets_EWK_LO_PythiaDecay/RunIISummer15wmLHEGS/161010_152335/0000/SMP-RunIISummer15wmLHEGS-00029_122.root',
	'file:/eos/uscms/store/user/rasharma/WlvWjjVBF2jets_EWK_LO_PythiaDecay/RunIISummer15wmLHEGS/161010_152335/0000/SMP-RunIISummer15wmLHEGS-00029_123.root',
	'file:/eos/uscms/store/user/rasharma/WlvWjjVBF2jets_EWK_LO_PythiaDecay/RunIISummer15wmLHEGS/161010_152335/0000/SMP-RunIISummer15wmLHEGS-00029_124.root',
	'file:/eos/uscms/store/user/rasharma/WlvWjjVBF2jets_EWK_LO_PythiaDecay/RunIISummer15wmLHEGS/161010_152335/0000/SMP-RunIISummer15wmLHEGS-00029_125.root',
	'file:/eos/uscms/store/user/rasharma/WlvWjjVBF2jets_EWK_LO_PythiaDecay/RunIISummer15wmLHEGS/161010_152335/0000/SMP-RunIISummer15wmLHEGS-00029_126.root',
	'file:/eos/uscms/store/user/rasharma/WlvWjjVBF2jets_EWK_LO_PythiaDecay/RunIISummer15wmLHEGS/161010_152335/0000/SMP-RunIISummer15wmLHEGS-00029_128.root',
	'file:/eos/uscms/store/user/rasharma/WlvWjjVBF2jets_EWK_LO_PythiaDecay/RunIISummer15wmLHEGS/161010_152335/0000/SMP-RunIISummer15wmLHEGS-00029_12.root',
	'file:/eos/uscms/store/user/rasharma/WlvWjjVBF2jets_EWK_LO_PythiaDecay/RunIISummer15wmLHEGS/161010_152335/0000/SMP-RunIISummer15wmLHEGS-00029_130.root',
	'file:/eos/uscms/store/user/rasharma/WlvWjjVBF2jets_EWK_LO_PythiaDecay/RunIISummer15wmLHEGS/161010_152335/0000/SMP-RunIISummer15wmLHEGS-00029_133.root',
	'file:/eos/uscms/store/user/rasharma/WlvWjjVBF2jets_EWK_LO_PythiaDecay/RunIISummer15wmLHEGS/161010_152335/0000/SMP-RunIISummer15wmLHEGS-00029_134.root',
	'file:/eos/uscms/store/user/rasharma/WlvWjjVBF2jets_EWK_LO_PythiaDecay/RunIISummer15wmLHEGS/161010_152335/0000/SMP-RunIISummer15wmLHEGS-00029_135.root',
	'file:/eos/uscms/store/user/rasharma/WlvWjjVBF2jets_EWK_LO_PythiaDecay/RunIISummer15wmLHEGS/161010_152335/0000/SMP-RunIISummer15wmLHEGS-00029_136.root',
	'file:/eos/uscms/store/user/rasharma/WlvWjjVBF2jets_EWK_LO_PythiaDecay/RunIISummer15wmLHEGS/161010_152335/0000/SMP-RunIISummer15wmLHEGS-00029_137.root',
	'file:/eos/uscms/store/user/rasharma/WlvWjjVBF2jets_EWK_LO_PythiaDecay/RunIISummer15wmLHEGS/161010_152335/0000/SMP-RunIISummer15wmLHEGS-00029_138.root',
	'file:/eos/uscms/store/user/rasharma/WlvWjjVBF2jets_EWK_LO_PythiaDecay/RunIISummer15wmLHEGS/161010_152335/0000/SMP-RunIISummer15wmLHEGS-00029_13.root',
	'file:/eos/uscms/store/user/rasharma/WlvWjjVBF2jets_EWK_LO_PythiaDecay/RunIISummer15wmLHEGS/161010_152335/0000/SMP-RunIISummer15wmLHEGS-00029_141.root',
	'file:/eos/uscms/store/user/rasharma/WlvWjjVBF2jets_EWK_LO_PythiaDecay/RunIISummer15wmLHEGS/161010_152335/0000/SMP-RunIISummer15wmLHEGS-00029_143.root',
	'file:/eos/uscms/store/user/rasharma/WlvWjjVBF2jets_EWK_LO_PythiaDecay/RunIISummer15wmLHEGS/161010_152335/0000/SMP-RunIISummer15wmLHEGS-00029_144.root',
	'file:/eos/uscms/store/user/rasharma/WlvWjjVBF2jets_EWK_LO_PythiaDecay/RunIISummer15wmLHEGS/161010_152335/0000/SMP-RunIISummer15wmLHEGS-00029_146.root',
	'file:/eos/uscms/store/user/rasharma/WlvWjjVBF2jets_EWK_LO_PythiaDecay/RunIISummer15wmLHEGS/161010_152335/0000/SMP-RunIISummer15wmLHEGS-00029_147.root',
	'file:/eos/uscms/store/user/rasharma/WlvWjjVBF2jets_EWK_LO_PythiaDecay/RunIISummer15wmLHEGS/161010_152335/0000/SMP-RunIISummer15wmLHEGS-00029_148.root',
	'file:/eos/uscms/store/user/rasharma/WlvWjjVBF2jets_EWK_LO_PythiaDecay/RunIISummer15wmLHEGS/161010_152335/0000/SMP-RunIISummer15wmLHEGS-00029_14.root',
	'file:/eos/uscms/store/user/rasharma/WlvWjjVBF2jets_EWK_LO_PythiaDecay/RunIISummer15wmLHEGS/161010_152335/0000/SMP-RunIISummer15wmLHEGS-00029_155.root',
	'file:/eos/uscms/store/user/rasharma/WlvWjjVBF2jets_EWK_LO_PythiaDecay/RunIISummer15wmLHEGS/161010_152335/0000/SMP-RunIISummer15wmLHEGS-00029_156.root',
	'file:/eos/uscms/store/user/rasharma/WlvWjjVBF2jets_EWK_LO_PythiaDecay/RunIISummer15wmLHEGS/161010_152335/0000/SMP-RunIISummer15wmLHEGS-00029_157.root',
	'file:/eos/uscms/store/user/rasharma/WlvWjjVBF2jets_EWK_LO_PythiaDecay/RunIISummer15wmLHEGS/161010_152335/0000/SMP-RunIISummer15wmLHEGS-00029_158.root',
	'file:/eos/uscms/store/user/rasharma/WlvWjjVBF2jets_EWK_LO_PythiaDecay/RunIISummer15wmLHEGS/161010_152335/0000/SMP-RunIISummer15wmLHEGS-00029_159.root',
	'file:/eos/uscms/store/user/rasharma/WlvWjjVBF2jets_EWK_LO_PythiaDecay/RunIISummer15wmLHEGS/161010_152335/0000/SMP-RunIISummer15wmLHEGS-00029_15.root',
	'file:/eos/uscms/store/user/rasharma/WlvWjjVBF2jets_EWK_LO_PythiaDecay/RunIISummer15wmLHEGS/161010_152335/0000/SMP-RunIISummer15wmLHEGS-00029_160.root',
	'file:/eos/uscms/store/user/rasharma/WlvWjjVBF2jets_EWK_LO_PythiaDecay/RunIISummer15wmLHEGS/161010_152335/0000/SMP-RunIISummer15wmLHEGS-00029_161.root',
	'file:/eos/uscms/store/user/rasharma/WlvWjjVBF2jets_EWK_LO_PythiaDecay/RunIISummer15wmLHEGS/161010_152335/0000/SMP-RunIISummer15wmLHEGS-00029_162.root',
	'file:/eos/uscms/store/user/rasharma/WlvWjjVBF2jets_EWK_LO_PythiaDecay/RunIISummer15wmLHEGS/161010_152335/0000/SMP-RunIISummer15wmLHEGS-00029_163.root',
	'file:/eos/uscms/store/user/rasharma/WlvWjjVBF2jets_EWK_LO_PythiaDecay/RunIISummer15wmLHEGS/161010_152335/0000/SMP-RunIISummer15wmLHEGS-00029_164.root',
	'file:/eos/uscms/store/user/rasharma/WlvWjjVBF2jets_EWK_LO_PythiaDecay/RunIISummer15wmLHEGS/161010_152335/0000/SMP-RunIISummer15wmLHEGS-00029_165.root',
	'file:/eos/uscms/store/user/rasharma/WlvWjjVBF2jets_EWK_LO_PythiaDecay/RunIISummer15wmLHEGS/161010_152335/0000/SMP-RunIISummer15wmLHEGS-00029_166.root',
	'file:/eos/uscms/store/user/rasharma/WlvWjjVBF2jets_EWK_LO_PythiaDecay/RunIISummer15wmLHEGS/161010_152335/0000/SMP-RunIISummer15wmLHEGS-00029_167.root',
	'file:/eos/uscms/store/user/rasharma/WlvWjjVBF2jets_EWK_LO_PythiaDecay/RunIISummer15wmLHEGS/161010_152335/0000/SMP-RunIISummer15wmLHEGS-00029_168.root',
	'file:/eos/uscms/store/user/rasharma/WlvWjjVBF2jets_EWK_LO_PythiaDecay/RunIISummer15wmLHEGS/161010_152335/0000/SMP-RunIISummer15wmLHEGS-00029_169.root',
	'file:/eos/uscms/store/user/rasharma/WlvWjjVBF2jets_EWK_LO_PythiaDecay/RunIISummer15wmLHEGS/161010_152335/0000/SMP-RunIISummer15wmLHEGS-00029_16.root',
	'file:/eos/uscms/store/user/rasharma/WlvWjjVBF2jets_EWK_LO_PythiaDecay/RunIISummer15wmLHEGS/161010_152335/0000/SMP-RunIISummer15wmLHEGS-00029_170.root',
	'file:/eos/uscms/store/user/rasharma/WlvWjjVBF2jets_EWK_LO_PythiaDecay/RunIISummer15wmLHEGS/161010_152335/0000/SMP-RunIISummer15wmLHEGS-00029_171.root',
	'file:/eos/uscms/store/user/rasharma/WlvWjjVBF2jets_EWK_LO_PythiaDecay/RunIISummer15wmLHEGS/161010_152335/0000/SMP-RunIISummer15wmLHEGS-00029_172.root',
	'file:/eos/uscms/store/user/rasharma/WlvWjjVBF2jets_EWK_LO_PythiaDecay/RunIISummer15wmLHEGS/161010_152335/0000/SMP-RunIISummer15wmLHEGS-00029_173.root',
	'file:/eos/uscms/store/user/rasharma/WlvWjjVBF2jets_EWK_LO_PythiaDecay/RunIISummer15wmLHEGS/161010_152335/0000/SMP-RunIISummer15wmLHEGS-00029_174.root',
	'file:/eos/uscms/store/user/rasharma/WlvWjjVBF2jets_EWK_LO_PythiaDecay/RunIISummer15wmLHEGS/161010_152335/0000/SMP-RunIISummer15wmLHEGS-00029_175.root',
	'file:/eos/uscms/store/user/rasharma/WlvWjjVBF2jets_EWK_LO_PythiaDecay/RunIISummer15wmLHEGS/161010_152335/0000/SMP-RunIISummer15wmLHEGS-00029_176.root',
	'file:/eos/uscms/store/user/rasharma/WlvWjjVBF2jets_EWK_LO_PythiaDecay/RunIISummer15wmLHEGS/161010_152335/0000/SMP-RunIISummer15wmLHEGS-00029_177.root',
	'file:/eos/uscms/store/user/rasharma/WlvWjjVBF2jets_EWK_LO_PythiaDecay/RunIISummer15wmLHEGS/161010_152335/0000/SMP-RunIISummer15wmLHEGS-00029_178.root',
	'file:/eos/uscms/store/user/rasharma/WlvWjjVBF2jets_EWK_LO_PythiaDecay/RunIISummer15wmLHEGS/161010_152335/0000/SMP-RunIISummer15wmLHEGS-00029_179.root',
	'file:/eos/uscms/store/user/rasharma/WlvWjjVBF2jets_EWK_LO_PythiaDecay/RunIISummer15wmLHEGS/161010_152335/0000/SMP-RunIISummer15wmLHEGS-00029_17.root',
	'file:/eos/uscms/store/user/rasharma/WlvWjjVBF2jets_EWK_LO_PythiaDecay/RunIISummer15wmLHEGS/161010_152335/0000/SMP-RunIISummer15wmLHEGS-00029_180.root',
	'file:/eos/uscms/store/user/rasharma/WlvWjjVBF2jets_EWK_LO_PythiaDecay/RunIISummer15wmLHEGS/161010_152335/0000/SMP-RunIISummer15wmLHEGS-00029_181.root',
	'file:/eos/uscms/store/user/rasharma/WlvWjjVBF2jets_EWK_LO_PythiaDecay/RunIISummer15wmLHEGS/161010_152335/0000/SMP-RunIISummer15wmLHEGS-00029_182.root',
	'file:/eos/uscms/store/user/rasharma/WlvWjjVBF2jets_EWK_LO_PythiaDecay/RunIISummer15wmLHEGS/161010_152335/0000/SMP-RunIISummer15wmLHEGS-00029_183.root',
	'file:/eos/uscms/store/user/rasharma/WlvWjjVBF2jets_EWK_LO_PythiaDecay/RunIISummer15wmLHEGS/161010_152335/0000/SMP-RunIISummer15wmLHEGS-00029_184.root',
	'file:/eos/uscms/store/user/rasharma/WlvWjjVBF2jets_EWK_LO_PythiaDecay/RunIISummer15wmLHEGS/161010_152335/0000/SMP-RunIISummer15wmLHEGS-00029_185.root',
	'file:/eos/uscms/store/user/rasharma/WlvWjjVBF2jets_EWK_LO_PythiaDecay/RunIISummer15wmLHEGS/161010_152335/0000/SMP-RunIISummer15wmLHEGS-00029_186.root',
	'file:/eos/uscms/store/user/rasharma/WlvWjjVBF2jets_EWK_LO_PythiaDecay/RunIISummer15wmLHEGS/161010_152335/0000/SMP-RunIISummer15wmLHEGS-00029_187.root',
	'file:/eos/uscms/store/user/rasharma/WlvWjjVBF2jets_EWK_LO_PythiaDecay/RunIISummer15wmLHEGS/161010_152335/0000/SMP-RunIISummer15wmLHEGS-00029_189.root',
	'file:/eos/uscms/store/user/rasharma/WlvWjjVBF2jets_EWK_LO_PythiaDecay/RunIISummer15wmLHEGS/161010_152335/0000/SMP-RunIISummer15wmLHEGS-00029_18.root',
	'file:/eos/uscms/store/user/rasharma/WlvWjjVBF2jets_EWK_LO_PythiaDecay/RunIISummer15wmLHEGS/161010_152335/0000/SMP-RunIISummer15wmLHEGS-00029_190.root',
	'file:/eos/uscms/store/user/rasharma/WlvWjjVBF2jets_EWK_LO_PythiaDecay/RunIISummer15wmLHEGS/161010_152335/0000/SMP-RunIISummer15wmLHEGS-00029_191.root',
	'file:/eos/uscms/store/user/rasharma/WlvWjjVBF2jets_EWK_LO_PythiaDecay/RunIISummer15wmLHEGS/161010_152335/0000/SMP-RunIISummer15wmLHEGS-00029_192.root',
	'file:/eos/uscms/store/user/rasharma/WlvWjjVBF2jets_EWK_LO_PythiaDecay/RunIISummer15wmLHEGS/161010_152335/0000/SMP-RunIISummer15wmLHEGS-00029_193.root',
	'file:/eos/uscms/store/user/rasharma/WlvWjjVBF2jets_EWK_LO_PythiaDecay/RunIISummer15wmLHEGS/161010_152335/0000/SMP-RunIISummer15wmLHEGS-00029_194.root',
	'file:/eos/uscms/store/user/rasharma/WlvWjjVBF2jets_EWK_LO_PythiaDecay/RunIISummer15wmLHEGS/161010_152335/0000/SMP-RunIISummer15wmLHEGS-00029_195.root',
	'file:/eos/uscms/store/user/rasharma/WlvWjjVBF2jets_EWK_LO_PythiaDecay/RunIISummer15wmLHEGS/161010_152335/0000/SMP-RunIISummer15wmLHEGS-00029_196.root',
	'file:/eos/uscms/store/user/rasharma/WlvWjjVBF2jets_EWK_LO_PythiaDecay/RunIISummer15wmLHEGS/161010_152335/0000/SMP-RunIISummer15wmLHEGS-00029_197.root',
	'file:/eos/uscms/store/user/rasharma/WlvWjjVBF2jets_EWK_LO_PythiaDecay/RunIISummer15wmLHEGS/161010_152335/0000/SMP-RunIISummer15wmLHEGS-00029_198.root',
	'file:/eos/uscms/store/user/rasharma/WlvWjjVBF2jets_EWK_LO_PythiaDecay/RunIISummer15wmLHEGS/161010_152335/0000/SMP-RunIISummer15wmLHEGS-00029_199.root',
	'file:/eos/uscms/store/user/rasharma/WlvWjjVBF2jets_EWK_LO_PythiaDecay/RunIISummer15wmLHEGS/161010_152335/0000/SMP-RunIISummer15wmLHEGS-00029_19.root',
	'file:/eos/uscms/store/user/rasharma/WlvWjjVBF2jets_EWK_LO_PythiaDecay/RunIISummer15wmLHEGS/161010_152335/0000/SMP-RunIISummer15wmLHEGS-00029_1.root',
	'file:/eos/uscms/store/user/rasharma/WlvWjjVBF2jets_EWK_LO_PythiaDecay/RunIISummer15wmLHEGS/161010_152335/0000/SMP-RunIISummer15wmLHEGS-00029_200.root',
	'file:/eos/uscms/store/user/rasharma/WlvWjjVBF2jets_EWK_LO_PythiaDecay/RunIISummer15wmLHEGS/161010_152335/0000/SMP-RunIISummer15wmLHEGS-00029_20.root',
	'file:/eos/uscms/store/user/rasharma/WlvWjjVBF2jets_EWK_LO_PythiaDecay/RunIISummer15wmLHEGS/161010_152335/0000/SMP-RunIISummer15wmLHEGS-00029_21.root',
	'file:/eos/uscms/store/user/rasharma/WlvWjjVBF2jets_EWK_LO_PythiaDecay/RunIISummer15wmLHEGS/161010_152335/0000/SMP-RunIISummer15wmLHEGS-00029_23.root',
	'file:/eos/uscms/store/user/rasharma/WlvWjjVBF2jets_EWK_LO_PythiaDecay/RunIISummer15wmLHEGS/161010_152335/0000/SMP-RunIISummer15wmLHEGS-00029_24.root',
	'file:/eos/uscms/store/user/rasharma/WlvWjjVBF2jets_EWK_LO_PythiaDecay/RunIISummer15wmLHEGS/161010_152335/0000/SMP-RunIISummer15wmLHEGS-00029_25.root',
	'file:/eos/uscms/store/user/rasharma/WlvWjjVBF2jets_EWK_LO_PythiaDecay/RunIISummer15wmLHEGS/161010_152335/0000/SMP-RunIISummer15wmLHEGS-00029_26.root',
	'file:/eos/uscms/store/user/rasharma/WlvWjjVBF2jets_EWK_LO_PythiaDecay/RunIISummer15wmLHEGS/161010_152335/0000/SMP-RunIISummer15wmLHEGS-00029_27.root',
	'file:/eos/uscms/store/user/rasharma/WlvWjjVBF2jets_EWK_LO_PythiaDecay/RunIISummer15wmLHEGS/161010_152335/0000/SMP-RunIISummer15wmLHEGS-00029_28.root',
	'file:/eos/uscms/store/user/rasharma/WlvWjjVBF2jets_EWK_LO_PythiaDecay/RunIISummer15wmLHEGS/161010_152335/0000/SMP-RunIISummer15wmLHEGS-00029_29.root',
	'file:/eos/uscms/store/user/rasharma/WlvWjjVBF2jets_EWK_LO_PythiaDecay/RunIISummer15wmLHEGS/161010_152335/0000/SMP-RunIISummer15wmLHEGS-00029_2.root',
	'file:/eos/uscms/store/user/rasharma/WlvWjjVBF2jets_EWK_LO_PythiaDecay/RunIISummer15wmLHEGS/161010_152335/0000/SMP-RunIISummer15wmLHEGS-00029_30.root',
	'file:/eos/uscms/store/user/rasharma/WlvWjjVBF2jets_EWK_LO_PythiaDecay/RunIISummer15wmLHEGS/161010_152335/0000/SMP-RunIISummer15wmLHEGS-00029_31.root',
	'file:/eos/uscms/store/user/rasharma/WlvWjjVBF2jets_EWK_LO_PythiaDecay/RunIISummer15wmLHEGS/161010_152335/0000/SMP-RunIISummer15wmLHEGS-00029_32.root',
	'file:/eos/uscms/store/user/rasharma/WlvWjjVBF2jets_EWK_LO_PythiaDecay/RunIISummer15wmLHEGS/161010_152335/0000/SMP-RunIISummer15wmLHEGS-00029_33.root',
	'file:/eos/uscms/store/user/rasharma/WlvWjjVBF2jets_EWK_LO_PythiaDecay/RunIISummer15wmLHEGS/161010_152335/0000/SMP-RunIISummer15wmLHEGS-00029_34.root',
	'file:/eos/uscms/store/user/rasharma/WlvWjjVBF2jets_EWK_LO_PythiaDecay/RunIISummer15wmLHEGS/161010_152335/0000/SMP-RunIISummer15wmLHEGS-00029_35.root',
	'file:/eos/uscms/store/user/rasharma/WlvWjjVBF2jets_EWK_LO_PythiaDecay/RunIISummer15wmLHEGS/161010_152335/0000/SMP-RunIISummer15wmLHEGS-00029_36.root',
	'file:/eos/uscms/store/user/rasharma/WlvWjjVBF2jets_EWK_LO_PythiaDecay/RunIISummer15wmLHEGS/161010_152335/0000/SMP-RunIISummer15wmLHEGS-00029_37.root',
	'file:/eos/uscms/store/user/rasharma/WlvWjjVBF2jets_EWK_LO_PythiaDecay/RunIISummer15wmLHEGS/161010_152335/0000/SMP-RunIISummer15wmLHEGS-00029_38.root',
	'file:/eos/uscms/store/user/rasharma/WlvWjjVBF2jets_EWK_LO_PythiaDecay/RunIISummer15wmLHEGS/161010_152335/0000/SMP-RunIISummer15wmLHEGS-00029_39.root',
	'file:/eos/uscms/store/user/rasharma/WlvWjjVBF2jets_EWK_LO_PythiaDecay/RunIISummer15wmLHEGS/161010_152335/0000/SMP-RunIISummer15wmLHEGS-00029_3.root',
	'file:/eos/uscms/store/user/rasharma/WlvWjjVBF2jets_EWK_LO_PythiaDecay/RunIISummer15wmLHEGS/161010_152335/0000/SMP-RunIISummer15wmLHEGS-00029_40.root',
	'file:/eos/uscms/store/user/rasharma/WlvWjjVBF2jets_EWK_LO_PythiaDecay/RunIISummer15wmLHEGS/161010_152335/0000/SMP-RunIISummer15wmLHEGS-00029_41.root',
	'file:/eos/uscms/store/user/rasharma/WlvWjjVBF2jets_EWK_LO_PythiaDecay/RunIISummer15wmLHEGS/161010_152335/0000/SMP-RunIISummer15wmLHEGS-00029_42.root',
	'file:/eos/uscms/store/user/rasharma/WlvWjjVBF2jets_EWK_LO_PythiaDecay/RunIISummer15wmLHEGS/161010_152335/0000/SMP-RunIISummer15wmLHEGS-00029_43.root',
	'file:/eos/uscms/store/user/rasharma/WlvWjjVBF2jets_EWK_LO_PythiaDecay/RunIISummer15wmLHEGS/161010_152335/0000/SMP-RunIISummer15wmLHEGS-00029_44.root',
	'file:/eos/uscms/store/user/rasharma/WlvWjjVBF2jets_EWK_LO_PythiaDecay/RunIISummer15wmLHEGS/161010_152335/0000/SMP-RunIISummer15wmLHEGS-00029_45.root',
	'file:/eos/uscms/store/user/rasharma/WlvWjjVBF2jets_EWK_LO_PythiaDecay/RunIISummer15wmLHEGS/161010_152335/0000/SMP-RunIISummer15wmLHEGS-00029_46.root',
	'file:/eos/uscms/store/user/rasharma/WlvWjjVBF2jets_EWK_LO_PythiaDecay/RunIISummer15wmLHEGS/161010_152335/0000/SMP-RunIISummer15wmLHEGS-00029_47.root',
	'file:/eos/uscms/store/user/rasharma/WlvWjjVBF2jets_EWK_LO_PythiaDecay/RunIISummer15wmLHEGS/161010_152335/0000/SMP-RunIISummer15wmLHEGS-00029_48.root',
	'file:/eos/uscms/store/user/rasharma/WlvWjjVBF2jets_EWK_LO_PythiaDecay/RunIISummer15wmLHEGS/161010_152335/0000/SMP-RunIISummer15wmLHEGS-00029_49.root',
	'file:/eos/uscms/store/user/rasharma/WlvWjjVBF2jets_EWK_LO_PythiaDecay/RunIISummer15wmLHEGS/161010_152335/0000/SMP-RunIISummer15wmLHEGS-00029_4.root',
	'file:/eos/uscms/store/user/rasharma/WlvWjjVBF2jets_EWK_LO_PythiaDecay/RunIISummer15wmLHEGS/161010_152335/0000/SMP-RunIISummer15wmLHEGS-00029_50.root',
	'file:/eos/uscms/store/user/rasharma/WlvWjjVBF2jets_EWK_LO_PythiaDecay/RunIISummer15wmLHEGS/161010_152335/0000/SMP-RunIISummer15wmLHEGS-00029_51.root',
	'file:/eos/uscms/store/user/rasharma/WlvWjjVBF2jets_EWK_LO_PythiaDecay/RunIISummer15wmLHEGS/161010_152335/0000/SMP-RunIISummer15wmLHEGS-00029_52.root',
	'file:/eos/uscms/store/user/rasharma/WlvWjjVBF2jets_EWK_LO_PythiaDecay/RunIISummer15wmLHEGS/161010_152335/0000/SMP-RunIISummer15wmLHEGS-00029_53.root',
	'file:/eos/uscms/store/user/rasharma/WlvWjjVBF2jets_EWK_LO_PythiaDecay/RunIISummer15wmLHEGS/161010_152335/0000/SMP-RunIISummer15wmLHEGS-00029_54.root',
	'file:/eos/uscms/store/user/rasharma/WlvWjjVBF2jets_EWK_LO_PythiaDecay/RunIISummer15wmLHEGS/161010_152335/0000/SMP-RunIISummer15wmLHEGS-00029_55.root',
	'file:/eos/uscms/store/user/rasharma/WlvWjjVBF2jets_EWK_LO_PythiaDecay/RunIISummer15wmLHEGS/161010_152335/0000/SMP-RunIISummer15wmLHEGS-00029_56.root',
	'file:/eos/uscms/store/user/rasharma/WlvWjjVBF2jets_EWK_LO_PythiaDecay/RunIISummer15wmLHEGS/161010_152335/0000/SMP-RunIISummer15wmLHEGS-00029_57.root',
	'file:/eos/uscms/store/user/rasharma/WlvWjjVBF2jets_EWK_LO_PythiaDecay/RunIISummer15wmLHEGS/161010_152335/0000/SMP-RunIISummer15wmLHEGS-00029_58.root',
	'file:/eos/uscms/store/user/rasharma/WlvWjjVBF2jets_EWK_LO_PythiaDecay/RunIISummer15wmLHEGS/161010_152335/0000/SMP-RunIISummer15wmLHEGS-00029_59.root',
	'file:/eos/uscms/store/user/rasharma/WlvWjjVBF2jets_EWK_LO_PythiaDecay/RunIISummer15wmLHEGS/161010_152335/0000/SMP-RunIISummer15wmLHEGS-00029_5.root',
	'file:/eos/uscms/store/user/rasharma/WlvWjjVBF2jets_EWK_LO_PythiaDecay/RunIISummer15wmLHEGS/161010_152335/0000/SMP-RunIISummer15wmLHEGS-00029_60.root',
	'file:/eos/uscms/store/user/rasharma/WlvWjjVBF2jets_EWK_LO_PythiaDecay/RunIISummer15wmLHEGS/161010_152335/0000/SMP-RunIISummer15wmLHEGS-00029_61.root',
	'file:/eos/uscms/store/user/rasharma/WlvWjjVBF2jets_EWK_LO_PythiaDecay/RunIISummer15wmLHEGS/161010_152335/0000/SMP-RunIISummer15wmLHEGS-00029_62.root',
	'file:/eos/uscms/store/user/rasharma/WlvWjjVBF2jets_EWK_LO_PythiaDecay/RunIISummer15wmLHEGS/161010_152335/0000/SMP-RunIISummer15wmLHEGS-00029_63.root',
	'file:/eos/uscms/store/user/rasharma/WlvWjjVBF2jets_EWK_LO_PythiaDecay/RunIISummer15wmLHEGS/161010_152335/0000/SMP-RunIISummer15wmLHEGS-00029_64.root',
	'file:/eos/uscms/store/user/rasharma/WlvWjjVBF2jets_EWK_LO_PythiaDecay/RunIISummer15wmLHEGS/161010_152335/0000/SMP-RunIISummer15wmLHEGS-00029_65.root',
	'file:/eos/uscms/store/user/rasharma/WlvWjjVBF2jets_EWK_LO_PythiaDecay/RunIISummer15wmLHEGS/161010_152335/0000/SMP-RunIISummer15wmLHEGS-00029_66.root',
	'file:/eos/uscms/store/user/rasharma/WlvWjjVBF2jets_EWK_LO_PythiaDecay/RunIISummer15wmLHEGS/161010_152335/0000/SMP-RunIISummer15wmLHEGS-00029_67.root',
	'file:/eos/uscms/store/user/rasharma/WlvWjjVBF2jets_EWK_LO_PythiaDecay/RunIISummer15wmLHEGS/161010_152335/0000/SMP-RunIISummer15wmLHEGS-00029_68.root',
	'file:/eos/uscms/store/user/rasharma/WlvWjjVBF2jets_EWK_LO_PythiaDecay/RunIISummer15wmLHEGS/161010_152335/0000/SMP-RunIISummer15wmLHEGS-00029_69.root',
	'file:/eos/uscms/store/user/rasharma/WlvWjjVBF2jets_EWK_LO_PythiaDecay/RunIISummer15wmLHEGS/161010_152335/0000/SMP-RunIISummer15wmLHEGS-00029_6.root',
	'file:/eos/uscms/store/user/rasharma/WlvWjjVBF2jets_EWK_LO_PythiaDecay/RunIISummer15wmLHEGS/161010_152335/0000/SMP-RunIISummer15wmLHEGS-00029_70.root',
	'file:/eos/uscms/store/user/rasharma/WlvWjjVBF2jets_EWK_LO_PythiaDecay/RunIISummer15wmLHEGS/161010_152335/0000/SMP-RunIISummer15wmLHEGS-00029_71.root',
	'file:/eos/uscms/store/user/rasharma/WlvWjjVBF2jets_EWK_LO_PythiaDecay/RunIISummer15wmLHEGS/161010_152335/0000/SMP-RunIISummer15wmLHEGS-00029_72.root',
	'file:/eos/uscms/store/user/rasharma/WlvWjjVBF2jets_EWK_LO_PythiaDecay/RunIISummer15wmLHEGS/161010_152335/0000/SMP-RunIISummer15wmLHEGS-00029_73.root',
	'file:/eos/uscms/store/user/rasharma/WlvWjjVBF2jets_EWK_LO_PythiaDecay/RunIISummer15wmLHEGS/161010_152335/0000/SMP-RunIISummer15wmLHEGS-00029_74.root',
	'file:/eos/uscms/store/user/rasharma/WlvWjjVBF2jets_EWK_LO_PythiaDecay/RunIISummer15wmLHEGS/161010_152335/0000/SMP-RunIISummer15wmLHEGS-00029_75.root',
	'file:/eos/uscms/store/user/rasharma/WlvWjjVBF2jets_EWK_LO_PythiaDecay/RunIISummer15wmLHEGS/161010_152335/0000/SMP-RunIISummer15wmLHEGS-00029_76.root',
	'file:/eos/uscms/store/user/rasharma/WlvWjjVBF2jets_EWK_LO_PythiaDecay/RunIISummer15wmLHEGS/161010_152335/0000/SMP-RunIISummer15wmLHEGS-00029_77.root',
	'file:/eos/uscms/store/user/rasharma/WlvWjjVBF2jets_EWK_LO_PythiaDecay/RunIISummer15wmLHEGS/161010_152335/0000/SMP-RunIISummer15wmLHEGS-00029_78.root',
	'file:/eos/uscms/store/user/rasharma/WlvWjjVBF2jets_EWK_LO_PythiaDecay/RunIISummer15wmLHEGS/161010_152335/0000/SMP-RunIISummer15wmLHEGS-00029_79.root',
	'file:/eos/uscms/store/user/rasharma/WlvWjjVBF2jets_EWK_LO_PythiaDecay/RunIISummer15wmLHEGS/161010_152335/0000/SMP-RunIISummer15wmLHEGS-00029_7.root',
	'file:/eos/uscms/store/user/rasharma/WlvWjjVBF2jets_EWK_LO_PythiaDecay/RunIISummer15wmLHEGS/161010_152335/0000/SMP-RunIISummer15wmLHEGS-00029_80.root',
	'file:/eos/uscms/store/user/rasharma/WlvWjjVBF2jets_EWK_LO_PythiaDecay/RunIISummer15wmLHEGS/161010_152335/0000/SMP-RunIISummer15wmLHEGS-00029_81.root',
	'file:/eos/uscms/store/user/rasharma/WlvWjjVBF2jets_EWK_LO_PythiaDecay/RunIISummer15wmLHEGS/161010_152335/0000/SMP-RunIISummer15wmLHEGS-00029_83.root',
	'file:/eos/uscms/store/user/rasharma/WlvWjjVBF2jets_EWK_LO_PythiaDecay/RunIISummer15wmLHEGS/161010_152335/0000/SMP-RunIISummer15wmLHEGS-00029_84.root',
	'file:/eos/uscms/store/user/rasharma/WlvWjjVBF2jets_EWK_LO_PythiaDecay/RunIISummer15wmLHEGS/161010_152335/0000/SMP-RunIISummer15wmLHEGS-00029_85.root',
	'file:/eos/uscms/store/user/rasharma/WlvWjjVBF2jets_EWK_LO_PythiaDecay/RunIISummer15wmLHEGS/161010_152335/0000/SMP-RunIISummer15wmLHEGS-00029_86.root',
	'file:/eos/uscms/store/user/rasharma/WlvWjjVBF2jets_EWK_LO_PythiaDecay/RunIISummer15wmLHEGS/161010_152335/0000/SMP-RunIISummer15wmLHEGS-00029_87.root',
	'file:/eos/uscms/store/user/rasharma/WlvWjjVBF2jets_EWK_LO_PythiaDecay/RunIISummer15wmLHEGS/161010_152335/0000/SMP-RunIISummer15wmLHEGS-00029_88.root',
	'file:/eos/uscms/store/user/rasharma/WlvWjjVBF2jets_EWK_LO_PythiaDecay/RunIISummer15wmLHEGS/161010_152335/0000/SMP-RunIISummer15wmLHEGS-00029_8.root',
	'file:/eos/uscms/store/user/rasharma/WlvWjjVBF2jets_EWK_LO_PythiaDecay/RunIISummer15wmLHEGS/161010_152335/0000/SMP-RunIISummer15wmLHEGS-00029_90.root',
	'file:/eos/uscms/store/user/rasharma/WlvWjjVBF2jets_EWK_LO_PythiaDecay/RunIISummer15wmLHEGS/161010_152335/0000/SMP-RunIISummer15wmLHEGS-00029_91.root',
	'file:/eos/uscms/store/user/rasharma/WlvWjjVBF2jets_EWK_LO_PythiaDecay/RunIISummer15wmLHEGS/161010_152335/0000/SMP-RunIISummer15wmLHEGS-00029_92.root',
	'file:/eos/uscms/store/user/rasharma/WlvWjjVBF2jets_EWK_LO_PythiaDecay/RunIISummer15wmLHEGS/161010_152335/0000/SMP-RunIISummer15wmLHEGS-00029_93.root',
	'file:/eos/uscms/store/user/rasharma/WlvWjjVBF2jets_EWK_LO_PythiaDecay/RunIISummer15wmLHEGS/161010_152335/0000/SMP-RunIISummer15wmLHEGS-00029_94.root',
	'file:/eos/uscms/store/user/rasharma/WlvWjjVBF2jets_EWK_LO_PythiaDecay/RunIISummer15wmLHEGS/161010_152335/0000/SMP-RunIISummer15wmLHEGS-00029_96.root',
	'file:/eos/uscms/store/user/rasharma/WlvWjjVBF2jets_EWK_LO_PythiaDecay/RunIISummer15wmLHEGS/161010_152335/0000/SMP-RunIISummer15wmLHEGS-00029_99.root',
	'file:/eos/uscms/store/user/rasharma/WlvWjjVBF2jets_EWK_LO_PythiaDecay/RunIISummer15wmLHEGS/161010_152335/0000/SMP-RunIISummer15wmLHEGS-00029_9.root'
	)
)

process.demo = cms.EDAnalyzer('GenAnalyzer',
	Verbose		=	cms.bool(False),

	genParticlesInputTag  = cms.InputTag("genParticles"),
	genJetsAK4jetsInputTag= cms.InputTag("ak4GenJets"),
	genJetsAK8jetsInputTag= cms.InputTag("ak8GenJets"),	#Not in use
	genMetTrueInputTag= cms.InputTag("genMetTrue"),		#not in use
	genMetCaloInputTag= cms.InputTag("genMetCalo")		#not in use

)

#process.GenAnalyzer = cms.EDProducer("GenAnalyzer",
#)

process.p = cms.Path(process.demo)
