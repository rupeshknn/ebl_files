#  - *-coding: utf - 8 - *-
# Python file exported with BEAMER Revision Number 7.2.0 (46e4f9cc09), Jul 18 2024, 06:40:16
# exported at 2024-Oct-08 17:58:01

# load necessary system libraries
import os
import sys

# set the path to the BEAMER python interface libraries
sys.path.append("C:/Program Files/BEAMER/v7.2.0_x64")

import BEAMERpy
try :

    # load the python BEAMER object
    BEAMER = BEAMERpy.GBEAMER()

    # set the PSF Archive Directories
    BEAMER.set_psf_archive_folder({ 'ArchivePath' : 'C:/Users/User/Documents/.GenISys/Repository/2D.Archive'})

    
    # Test Junction Single Die_top2rows
    gobj_1 = BEAMER.import_gds( 
             {'LayerSet' : '14(0), 15(0), 1(0)',
              'ImportBoxes' : True,
              'ImportZeroWidthPaths' : False,
              'LineWidth' : 0.000000,
              'KeepElementOrder' : False,
              'FlattenLayout' : False,
              'OverlapAndGapDetectionEnabled' : False,
              'OverlapAndGapDetectionMinSize' : 0.000000,
              'LoadTextElements' : False,
              'ConvertedTextSize' : 1.000000,
              'ConvertTextElementsToPolys' : False,
              'KeepPathElements' : False,
              'Circle' : False,
              'Ring' : False,
              'ArcBow' : False,
              'Sector' : False,
              'Ellipse' : False,
              'RotRect' : False,
              'Parallelogram' : False,
              'Quadrangle' : False,
              'MaxErrorForConversion' : 0.001000,
              'CurveDetection' : False,
              'MaxErrorForConversion' : 0.001000,
              'FileName' : 'Z:/rupesh/testjj_2rows/Test Junction Single Die_top2rows.gds'} )
    
    # Extract
    gobj_2 = BEAMER.extract_layer( gobj_1, 
             {'ExtentMode' : 'Default',
              'CellName' : '',
              'LayerSet' : '14(0), 15(0)',
              'RegionLayer' : '',
              'RegionLayerBehavior' : 'Clip',
              'ResultMode' : 'Region/Instances',
              'DoseClassificationShrink' : 'Automatic',
              'KeepRegionLayer' : False,
              'ExtractBoxes' : []} )
    
    # Flat
    gobj_3 = BEAMER.fracture( gobj_2, 
             {'FractureLayer' : '*',
              'KeepResolution' : True,
              'Resolution' : 0.001000,
              'BeamStepSize' : 1,
              'NumberSleeves' : 1,
              'SleevingSize' : 1,
              'SleeveBulkOverlap' : 0.000000,
              'SleevingLayer' : '*',
              'SleevingTargetLayer' : '',
              'CurveApproxTolerance' : 0.100000,
              'CurveTolerance' : 1.000000,
              'FractureAxis' : 'X_AND_Y',
              'FractureMode' : 'LRFT',
              'BssFracturing' : False,
              'SleeveGeneration' : False,
              'Symmetric Fracturing' : False,
              'FractureAngle' : 'AnyAngle',
              'FractureTolerance' : 1.000000,
              'FractureType' : 'Flat'} )
    
    # Overlap Removal
    gobj_4 = BEAMER.heal( gobj_3, 
             {'SoftFrame' : 0.300000,
              'HierarchicalProcessing' : True,
              'SelectedLayerSet' : '*',
              'LayerAssignment' : 'PerLayer',
              'ProcessingMode' : 'OverlapRemoval'} )
    
    # Split
    gobj_8 = gobj_4
    
    # 3D E-Beam Edge
    gobj_5 = BEAMER.pec_3d( gobj_8, 
             {'LayerPropertiesFile' : '**filename**',
              'ContrastCurveFile' : '**filename**',
              'UserdefinedDoseClassFile' : '**filename**',
              'MinFractureSizeMode' : 'Automatic',
              'PSFArchiveIdentifierString' : 'Substrate_Si_Thickness_700000_Energy_100_Layers__Resist_PMMA 100 nm_Z-Position_0.045_Electrons_2000000_Alpha_0_Beta_0_Eta_0_Gamma1_0_Nue1_0_Gamma2_0_Nue2_0_Simulator_mcTrace 1.0.0',
              'PSFType' : 'Numeric',
              'PSFFileName' : 'C:/Users/User/Downloads/Si_375um_MMA_600nm_PMMA_240nm_100kV_z401nm.lpsf',
              'BeamSize' : 0.010000,
              'DoseClassMode' : 'Accuracy',
              'MaxNumOfDoseClasses' : 256,
              'Accuracy' : 1.000000,
              'MinDoseFactor' : 0.010000,
              'MaxDoseFactor' : 10.000000,
              'UserDefinedSeparationValue' : False,
              'SeparationValue' : 0.100000,
              'FractureGrid' : 0.010000,
              'MinFractureSize' : 0.100000,
              'MinFractureSizeShortRange' : 0.100000,
              'LayerListForCorrection' : '*',
              'LayerListForFullCorrection' : '*',
              'LayerForFracture' : '*',
              'ContrastPartofLRPEC' : 100.000000,
              'WorkingRangeMin' : 0.000000,
              'WorkingRangeMax' : 1.000000,
              'SurfaceDefinitionMode' : 'RelativeThickness',
              '3dSurfaceErrorTolerance' : 1.000000,
              '3DPECMode' : 'Edge',
              'BaseDose' : 300.000000,
              'OriginalResistThickness' : 1.000000,
              'GrayScaleOffset' : 0.000000,
              'ZFracture' : False,
              'Mode' : 'Absorption Coefficient (a)',
              'AbsorptionUnBleached' : 0.000000,
              'AbsorptionBleached' : 0.000000,
              'RefractiveIndex' : 1.000000,
              'RefractiveIndexBleached' : 1.000000,
              'BeamDivergence' : False,
              'Wavelength' : 0.000000,
              'FocusOffset' : 0.000000,
              'OverdoseFactor' : 1.000000,
              'MidRangeActivationThreshold' : 5.000000,
              'SingleLineBeamWidth' : 0.000000,
              'IncludeSRCorrection' : True,
              'HierarchicShortRangePEC' : False,
              'HierarchicLongRangePEC' : False,
              'ConvergenceOutput' : False,
              'IncludeLateralDevelopment' : False,
              'ThicknessFormula' : '',
              'LateralDevelopmentGrid' : 0.100000,
              'CellsToKeep' : '',
              'LayerPropertiesList' : [['14(0)',' .25'], ['15(0)',' 1.000000']],
              'ContrastCurveFromDatabase' : False,
              'ResistName' : '',
              'DeveloperName' : '',
              'Use2dLateralDevelopmentBias' : False} )
    
    # 20240726_testJJ_matrix
    gobj_9 = BEAMER.import_gds( 
             {'LayerSet' : '*',
              'ImportBoxes' : True,
              'ImportZeroWidthPaths' : False,
              'LineWidth' : 0.000000,
              'KeepElementOrder' : False,
              'FlattenLayout' : False,
              'OverlapAndGapDetectionEnabled' : False,
              'OverlapAndGapDetectionMinSize' : 0.000000,
              'LoadTextElements' : False,
              'ConvertedTextSize' : 1.000000,
              'ConvertTextElementsToPolys' : False,
              'KeepPathElements' : False,
              'Circle' : False,
              'Ring' : False,
              'ArcBow' : False,
              'Sector' : False,
              'Ellipse' : False,
              'RotRect' : False,
              'Parallelogram' : False,
              'Quadrangle' : False,
              'MaxErrorForConversion' : 0.001000,
              'CurveDetection' : False,
              'MaxErrorForConversion' : 0.001000,
              'FileName' : 'Z:/rupesh/testjj_2rows/20240726_testJJ_matrix.gds'} )
    
    # ChipPlace (1)
    gobj_11 = BEAMER.genjobdeck( [gobj_8, gobj_9], 
             {'SubstrateType' : 'Wafer Circle',
              'SubstrateSize' : 3.000000,
              'UserDefineSubstrateName' : '',
              'ExportChipAgainstSubstratePosition' : 'Write all chips / Ignore substrate boundaries',
              'GenJobdeckArrays' : [[1, '', 0.000000, 0.000000, 7, 7, 8000.000000, 8000.000000, 'Center'], [2, '', 0.000000, 0.000000, 1, 1, 100.000000, 100.000000, 'Center']],
              'GenJobdeckChips' : [['Port_0_3D E-Beam Edge', '', 1, '(*, *, x1)', 0.000000, 0.000000], ['Port_1_20240726_testJJ_matrix_20240726_testJJ_matrix.gds', '', 2, '(*,*,x1)', 0.000000, 0.000000]],
              'GenJobdeckTexts' : [],
              'GenJobdeckSubarrays' : []} )
    
    # Split (2)
    gobj_13 = gobj_5
    
    # 20240726_testJJ_matrix_top2rows
    gobj_10 = BEAMER.export_gds( gobj_11, 
             {'FileName' : 'Z:/rupesh/testjj_2rows/20240726_testJJ_matrix_top2rows.gds',
              'LayerSet' : '*',
              'FlattenLeaves' : 0,
              'SubtreeSelected' : False,
              'MaximumPolygonVertices' : 1024,
              'DoseMapping' : 'Void',
              'UseOutputTopCellName' : False,
              'TopCellName' : '',
              'CurveApproximationAccuracy' : 0.001000} )
    
    # ChipPlace
    gobj_6 = BEAMER.genjobdeck( [gobj_13], 
             {'SubstrateType' : 'Wafer Circle',
              'SubstrateSize' : 3.000000,
              'UserDefineSubstrateName' : '',
              'ExportChipAgainstSubstratePosition' : 'Write all chips / Ignore substrate boundaries',
              'GenJobdeckArrays' : [[1, '', 0.000000, 0.000000, 7, 7, 8000.000000, 8000.000000, 'Center'], [2, '', 0.000000, 0.000000, 1, 1, 100.000000, 100.000000, 'Center']],
              'GenJobdeckChips' : [['Port_0_3D E-Beam Edge', '', 1, '(*, *, x1)', 0.000000, 0.000000]],
              'GenJobdeckTexts' : [],
              'GenJobdeckSubarrays' : []} )
    
    # Split (1)
    gobj_12 = gobj_6
    
    # Test_Junction_Single_Die_2rows_temp
    gobj_7 = BEAMER.export_con( gobj_12, 
             {'FileName' : 'Z:/rupesh/Test_Junction_Single_Die_2rows_temp.con',
              'ExtentMode' : 'Default',
              'LowerLeftX' : 0.000000,
              'LowerLeftY' : 0.000000,
              'UpperRightX' : 0.000000,
              'UpperRightY' : 0.000000,
              'ReplaceFiles' : True,
              'GenerateFolder' : True,
              'FormatType' : 'SCON',
              'MaximumFieldSize' : 1000,
              'DotNumber' : 1000000,
              'FieldSizeX' : 1000.000,
              'FieldSizeY' : 1000.000,
              'PitchSize' : 5,
              'BaseDoseTime' : 0.455,
              'RectangleOrientation' : 'X_AND_Y',
              'GenerateCCCFiles' : True,
              'GenerateCPGData' : True,
              'GenerateParallelograms' : False,
              'FieldTraversalType' : 'Floating',
              'KeepLayoutPosition' : True,
              'FractureMode' : 'Curved',
              'CurveTolerance' : 1.000000,
              'SymmetricFracturing' : False,
              'ShotPitchAlignment' : 'NONE',
              'FeatureOrderingType' : 'Standard',
              'SortedOrderLayer' : '*',
              'CompRegSize' : 1000.000,
              'RegTraversal' : 'MeanderX',
              'DoseMapping' : 'DoseToTime',
              'NumberGlobalMarks' : 2,
              'MarkA_X' : 0.000000,
              'MarkA_Y' : -24,
              'MarkB_X' : 0.000000,
              'MarkB_Y' : 24,
              'FieldOverlapX' : 0.000000,
              'FieldOverlapY' : 0.000000,
              'MultipassMode' : 'Single Pass'} )
except BEAMERpy.GError as e :
    print("exception caught")
    print(e)
