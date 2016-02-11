from .stage01_isotopomer_peakSpectrum_postgresql_models import *
from SBaaS_LIMS.lims_experiment_postgresql_models import *
from SBaaS_LIMS.lims_sample_postgresql_models import *

from SBaaS_base.sbaas_base_query_update import sbaas_base_query_update
from SBaaS_base.sbaas_base_query_drop import sbaas_base_query_drop
from SBaaS_base.sbaas_base_query_initialize import sbaas_base_query_initialize
from SBaaS_base.sbaas_base_query_insert import sbaas_base_query_insert
from SBaaS_base.sbaas_base_query_select import sbaas_base_query_select
from SBaaS_base.sbaas_base_query_delete import sbaas_base_query_delete

from SBaaS_base.sbaas_template_query import sbaas_template_query

class stage01_isotopomer_peakSpectrum_query(sbaas_template_query):
    def initialize_supportedTables(self):
        '''Set the supported tables dict for 
        '''
        tables_supported = {'data_stage01_isotopomer_peakSpectrum':data_stage01_isotopomer_peakSpectrum,
                        };
        self.set_supportedTables(tables_supported);
    def initialize_dataStage01_isotopomer_peakSpectrum(self):
        try:
            data_stage01_isotopomer_peakSpectrum.__table__.create(self.engine,True);
        except SQLAlchemyError as e:
            print(e);
    def drop_dataStage01_isotopomer_peakSpectrum(self):
        try:
            data_stage01_isotopomer_peakSpectrum.__table__.drop(self.engine,True);
        except SQLAlchemyError as e:
            print(e);
    def reset_dataStage01_isotopomer_peakSpectrum(self,experiment_id_I = None):
        try:
            if experiment_id_I:
                reset = self.session.query(data_stage01_isotopomer_peakSpectrum).filter(data_stage01_isotopomer_peakSpectrum.experiment_id.like(experiment_id_I)).delete(synchronize_session=False);
                self.session.commit();
        except SQLAlchemyError as e:
            print(e);
    # query sample names from data_stage01_isotopomer_peakSpectrum
    def get_sampleNames_experimentIDAndSampleType_peakSpectrum(self,experiment_id_I,sample_type_I):
        '''Querry sample names (i.e. unknowns) that are used from
        the experiment'''
        try:
            sample_names = self.session.query(data_stage01_isotopomer_peakSpectrum.sample_name).filter(
                    data_stage01_isotopomer_peakSpectrum.experiment_id.like(experiment_id_I),
                    data_stage01_isotopomer_peakSpectrum.sample_type.like(sample_type_I)).group_by(
                    data_stage01_isotopomer_peakSpectrum.sample_name).order_by(
                    data_stage01_isotopomer_peakSpectrum.sample_name.asc()).all();
            sample_names_O = [];
            for sn in sample_names: sample_names_O.append(sn.sample_name);
            return sample_names_O;
        except SQLAlchemyError as e:
            print(e);
    def get_sampleNames_experimentIDAndSampleTypeAndSampleNameAbbreviation_peakSpectrum(self,experiment_id_I,sample_type_I,sample_name_abbreviation_I):
        '''Querry sample names (i.e. unknowns) that are used from
        the experiment'''
        try:
            sample_names = self.session.query(data_stage01_isotopomer_peakSpectrum.sample_name).filter(
                    data_stage01_isotopomer_peakSpectrum.experiment_id.like(experiment_id_I),
                    data_stage01_isotopomer_peakSpectrum.sample_type.like(sample_type_I),
                    data_stage01_isotopomer_peakSpectrum.sample_name_abbreviation.like(sample_name_abbreviation_I)).group_by(
                    data_stage01_isotopomer_peakSpectrum.sample_name).order_by(
                    data_stage01_isotopomer_peakSpectrum.sample_name.asc()).all();
            sample_names_O = [];
            for sn in sample_names: sample_names_O.append(sn.sample_name);
            return sample_names_O;
        except SQLAlchemyError as e:
            print(e);
    def get_sampleNameAndDilution_experimentIDAndTimePointAndSampleNameAbbreviationAndScanType_peakSpectrum(self,experiment_id_I,time_point_I,sample_name_abbreviation_I,scan_type_I,sample_replicate_I):
        '''Querry sample name and dilution from the experiment
        by time-point, sample name abbreviation, scan type, and replicate numbers'''
        try:
            sample_name = self.session.query(data_stage01_isotopomer_peakSpectrum.sample_name,
                    sample.sample_dilution).filter(
                    data_stage01_isotopomer_peakSpectrum.sample_name_abbreviation.like(sample_name_abbreviation_I),
                    data_stage01_isotopomer_peakSpectrum.time_point.like(time_point_I),
                    data_stage01_isotopomer_peakSpectrum.scan_type.like(scan_type_I),
                    data_stage01_isotopomer_peakSpectrum.experiment_id.like(experiment_id_I),
                    data_stage01_isotopomer_peakSpectrum.replicate_number == sample_replicate_I,
                    data_stage01_isotopomer_peakSpectrum.used_,
                    data_stage01_isotopomer_peakSpectrum.sample_name.like(sample.sample_name)).group_by(
                    data_stage01_isotopomer_peakSpectrum.sample_name,
                    sample.sample_dilution).all();
            sample_name_O = None;
            dilution_O = None;
            if not sample_name: 
                print('no sample name and dilution found for experiment_id\ttime_point\tsample_name_abbreviation\tscan_type\tsample_replicate');
                print((experiment_id_I + '\t'+ time_point_I + '\t'+ sample_name_abbreviation_I + '\t'+ scan_type_I + '\t'+ str(sample_replicate_I)));
            else:
                sample_name_O = sample_name[0][0];
                dilution_O = sample_name[0][1];
            return sample_name_O,dilution_O;
        except SQLAlchemyError as e:
            print(e);
    # query sample name abbreviations from data_stage01_isotopomer_peakSpectrum
    def get_sampleNameAbbreviations_experimentIDAndSampleTypeAndTimePoint_peakSpectrum(self,experiment_id_I,sample_type_I,time_point_I):
        '''Querry sample name abbreviations from the experiment by sample type and time point'''
        try:
            sample_name_abbreviations = self.session.query(sample_description.sample_name_abbreviation).filter(
                    data_stage01_isotopomer_peakSpectrum.time_point.like(time_point_I),
                    data_stage01_isotopomer_peakSpectrum.sample_type.like(sample_type_I),
                    data_stage01_isotopomer_peakSpectrum.experiment_id.like(experiment_id_I),
                    data_stage01_isotopomer_peakSpectrum.sample_name.like(sample.sample_name),
                    sample.sample_id.like(sample_description.sample_id),
                    data_stage01_isotopomer_peakSpectrum.used_).group_by(
                    sample_description.sample_name_abbreviation).order_by(
                    sample_description.sample_name_abbreviation.asc()).all();
            sample_name_abbreviations_O = [];
            if not sample_name_abbreviations: print(('no sample name abbreviations found for experiment: ' + experiment_id_I\
                + ' and time-point: ' + time_point_I + ' and sample type: ' + sample_type_I));
            else:
                for sna in sample_name_abbreviations:
                    sample_name_abbreviations_O.append(sna[0]);
            return sample_name_abbreviations_O;
        except SQLAlchemyError as e:
            print(e);
    def get_sampleNameAbbreviationsAndTimePointAndReplicateNumber_experimentIDAndSampleName_peakSpectrum(self,experiment_id_I,sample_name_I):
        '''Querry sample name abbreviations, time points and replicate numbers from
        the experiment by sample name'''
        try:
            sample_name_abbreviations = self.session.query(sample_description.sample_name_abbreviation,
                    sample_description.time_point,
                    sample_description.sample_replicate).filter(
                    data_stage01_isotopomer_peakSpectrum.sample_name.like(sample_name_I),
                    data_stage01_isotopomer_peakSpectrum.experiment_id.like(experiment_id_I),
                    data_stage01_isotopomer_peakSpectrum.sample_name.like(sample.sample_name),
                    sample.sample_id.like(sample_description.sample_id)).group_by(
                    sample_description.sample_name_abbreviation,
                    sample_description.time_point,
                    sample_description.sample_replicate).order_by(
                    sample_description.sample_name_abbreviation.asc()).all();
            sample_name_abbreviations_O = None;
            time_points_O = None;
            sample_replicates_O = None;
            if not sample_name_abbreviations: exit('bad query result: get_sampleNameAbbreviationsAndOther_experimentIDAndSampleName_peakSpectrum');
            sample_name_abbreviations_O=sample_name_abbreviations[0][0];
            time_points_O=sample_name_abbreviations[0][1];
            sample_replicates_O=sample_name_abbreviations[0][2];
            return sample_name_abbreviations_O,time_points_O,sample_replicates_O;
        except SQLAlchemyError as e:
            print(e);
    def get_sampleNameAbbreviationsAndOther_experimentIDAndSampleName_peakSpectrum(self,experiment_id_I,sample_name_I):
        '''Querry sample name abbreviations, time points, dilutions, and replicate numbers from
        the experiment by sample name'''
        try:
            sample_name_abbreviations = self.session.query(sample_description.sample_name_abbreviation,
                    sample_description.time_point,
                    sample.sample_dilution,
                    sample_description.sample_replicate).filter(
                    data_stage01_isotopomer_peakSpectrum.sample_name.like(sample_name_I),
                    data_stage01_isotopomer_peakSpectrum.experiment_id.like(experiment_id_I),
                    data_stage01_isotopomer_peakSpectrum.sample_name.like(sample.sample_name),
                    sample.sample_id.like(sample_description.sample_id)).group_by(
                    sample_description.sample_name_abbreviation,
                    sample_description.time_point,
                    sample.sample_dilution,
                    sample_description.sample_replicate).order_by(
                    sample_description.sample_name_abbreviation.asc()).all();
            sample_name_abbreviations_O = None;
            time_points_O = None;
            dilutions_O = None;
            sample_replicates_O = None;
            if not sample_name_abbreviations: exit('bad query result: get_sampleNameAbbreviationsAndOther_experimentIDAndSampleName_peakSpectrum');
            sample_name_abbreviations_O=sample_name_abbreviations[0][0];
            time_points_O=sample_name_abbreviations[0][1];
            dilutions_O=sample_name_abbreviations[0][2];
            sample_replicates_O=sample_name_abbreviations[0][3];
            return sample_name_abbreviations_O,time_points_O,dilutions_O,sample_replicates_O;
        except SQLAlchemyError as e:
            print(e);
    # query time_points from data_stage01_isotopomer_peakSpectrum
    def get_timePoints_experimentID_peakSpectrum(self,experiment_id_I):
        '''time points from the experiment'''
        try:
            timepoints = self.session.query(
                    sample_description.time_point).filter(
                    data_stage01_isotopomer_peakSpectrum.experiment_id.like(experiment_id_I),
                    data_stage01_isotopomer_peakSpectrum.sample_name.like(sample.sample_name),
                    sample.sample_id.like(sample_description.sample_id),
                    data_stage01_isotopomer_peakSpectrum.used_).group_by(
                    sample_description.time_point).order_by(
                    sample_description.time_point.asc()).all();
            time_points_O = [];
            sample_replicates_O = None;
            if not timepoints: print(('no time points found for experiment: ' + experiment_id_I));
            else:
                for tp in timepoints:
                    time_points_O.append(tp[0]);
            return time_points_O;
        except SQLAlchemyError as e:
            print(e);
    # query met_id, precursor formula from data_stage01_isotopomer_peakSpectrum
    def get_metIDAndPrecursorFormulaAndScanType_experimentIDAndSampleName_peakSpectrum(self,experiment_id_I,sample_name_I):
        '''Querry met_id, precursor formula that are used for the experiment'''
        try:
            component_names = self.session.query(data_stage01_isotopomer_peakSpectrum.met_id,
                    data_stage01_isotopomer_peakSpectrum.precursor_formula,
                    data_stage01_isotopomer_peakSpectrum.scan_type).filter(
                    data_stage01_isotopomer_peakSpectrum.sample_name.like(sample_name_I),
                    data_stage01_isotopomer_peakSpectrum.experiment_id.like(experiment_id_I)).group_by(
                    data_stage01_isotopomer_peakSpectrum.met_id,
                    data_stage01_isotopomer_peakSpectrum.precursor_formula,
                    data_stage01_isotopomer_peakSpectrum.scan_type).order_by(
                    data_stage01_isotopomer_peakSpectrum.met_id.asc(),
                    data_stage01_isotopomer_peakSpectrum.precursor_formula).all();
            met_ids_O = [];
            precursor_formulas_O = [];
            scan_type_O = [];
            if not component_names: exit('bad query result: get_metIDAndPrecursorFormula_experimentIDAndSampleName_peakSpectrum');
            for cn in component_names:
                met_ids_O.append(cn.met_id);
                precursor_formulas_O.append(cn.precursor_formula);
                scan_type_O.append(cn.scan_type);
            return met_ids_O, precursor_formulas_O, scan_type_O;
        except SQLAlchemyError as e:
            print(e);
    def get_metIDAndPrecursorFormula_experimentIDAndSampleNameAndScanType_peakSpectrum(self,experiment_id_I,sample_name_I,scan_type_I):
        '''Querry met_id, precursor formula that are used for the experiment'''
        try:
            component_names = self.session.query(data_stage01_isotopomer_peakSpectrum.met_id,
                    data_stage01_isotopomer_peakSpectrum.precursor_formula).filter(
                    data_stage01_isotopomer_peakSpectrum.sample_name.like(sample_name_I),
                    data_stage01_isotopomer_peakSpectrum.experiment_id.like(experiment_id_I),
                    data_stage01_isotopomer_peakSpectrum.scan_type.like(scan_type_I)).group_by(
                    data_stage01_isotopomer_peakSpectrum.met_id,
                    data_stage01_isotopomer_peakSpectrum.precursor_formula).order_by(
                    data_stage01_isotopomer_peakSpectrum.met_id.asc(),
                    data_stage01_isotopomer_peakSpectrum.precursor_formula).all();
            met_ids_O = [];
            precursor_formulas_O = [];
            if not component_names: exit('bad query result: get_metIDAndPrecursorFormula_experimentIDAndSampleNameAndScanType_peakSpectrum');
            for cn in component_names:
                met_ids_O.append(cn.met_id);
                precursor_formulas_O.append(cn.precursor_formula);
            return met_ids_O, precursor_formulas_O;
        except SQLAlchemyError as e:
            print(e);
    def get_metIDAndPrecursorFormulaAndMass_experimentIDAndSampleNameAndScanType_peakSpectrum(self,experiment_id_I,sample_name_I,scan_type_I):
        '''Querry met_id, precursor formula that are used for the experiment'''
        try:
            component_names = self.session.query(data_stage01_isotopomer_peakSpectrum.met_id,
                    data_stage01_isotopomer_peakSpectrum.precursor_formula,
                    data_stage01_isotopomer_peakSpectrum.precursor_mass).filter(
                    data_stage01_isotopomer_peakSpectrum.sample_name.like(sample_name_I),
                    data_stage01_isotopomer_peakSpectrum.experiment_id.like(experiment_id_I),
                    data_stage01_isotopomer_peakSpectrum.scan_type.like(scan_type_I)).group_by(
                    data_stage01_isotopomer_peakSpectrum.met_id,
                    data_stage01_isotopomer_peakSpectrum.precursor_formula,
                    data_stage01_isotopomer_peakSpectrum.precursor_mass).order_by(
                    data_stage01_isotopomer_peakSpectrum.met_id.asc(),
                    data_stage01_isotopomer_peakSpectrum.precursor_mass.asc(),
                    data_stage01_isotopomer_peakSpectrum.precursor_formula).all();
            met_ids_O = [];
            precursor_formulas_O = [];
            precursor_mass_O = [];
            if not component_names: exit('bad query result: get_metIDAndPrecursorFormulaAndMass_experimentIDAndSampleNameAndScanType_peakSpectrum');
            for cn in component_names:
                met_ids_O.append(cn.met_id);
                precursor_formulas_O.append(cn.precursor_formula);
                precursor_mass_O.append(cn.precursor_mass);
            return met_ids_O, precursor_formulas_O, precursor_mass_O;
        except SQLAlchemyError as e:
            print(e);
    def get_metID_experimentIDAndTimePointAndSampleNameAbbreviationAndScanTypeAndReplicate_peakSpectrum(self,experiment_id_I,time_point_I,sample_name_abbreviation_I,scan_type_I,sample_replicate_I):
        '''Querry met_ids that are used for the experiment        
        by time-point, sample name abbreviation, scan type, and replicate numbers'''
        try:
            component_names = self.session.query(data_stage01_isotopomer_peakSpectrum.met_id).filter(
                    data_stage01_isotopomer_peakSpectrum.sample_name_abbreviation.like(sample_name_abbreviation_I),
                    data_stage01_isotopomer_peakSpectrum.time_point.like(time_point_I),
                    data_stage01_isotopomer_peakSpectrum.scan_type.like(scan_type_I),
                    data_stage01_isotopomer_peakSpectrum.experiment_id.like(experiment_id_I),
                    data_stage01_isotopomer_peakSpectrum.replicate_number == sample_replicate_I,
                    data_stage01_isotopomer_peakSpectrum.used_).group_by(
                    data_stage01_isotopomer_peakSpectrum.met_id).order_by(
                    data_stage01_isotopomer_peakSpectrum.met_id.asc()).all();
            met_ids_O = [];
            if not component_names:
                print('no met ids found for experiment_id\ttime_point\tsample_name_abbreviation\tscan_type\tsample_replicate');
                print((experiment_id_I + '\t'+ time_point_I + '\t'+ sample_name_abbreviation_I + '\t'+ scan_type_I + '\t'+ str(sample_replicate_I)));
            else:
                for cn in component_names:
                    met_ids_O.append(cn[0]);
            return met_ids_O;
        except SQLAlchemyError as e:
            print(e);
    def get_metID_experimentIDAndSampleNameAndScanType_peakSpectrum(self,experiment_id_I,sample_name_I,scan_type_I):
        '''Querry met_ids that are used for the experiment'''
        try:
            component_names = self.session.query(data_stage01_isotopomer_peakSpectrum.met_id).filter(
                    data_stage01_isotopomer_peakSpectrum.sample_name.like(sample_name_I),
                    data_stage01_isotopomer_peakSpectrum.experiment_id.like(experiment_id_I),
                    data_stage01_isotopomer_peakSpectrum.scan_type.like(scan_type_I)).group_by(
                    data_stage01_isotopomer_peakSpectrum.met_id).order_by(
                    data_stage01_isotopomer_peakSpectrum.met_id.asc()).all();
            met_ids_O = [];
            if not component_names: exit('bad query result: get_metID_experimentIDAndSampleNameAndScanType_peakSpectrum');
            for cn in component_names:
                met_ids_O.append(cn[0]);
            return met_ids_O;
        except SQLAlchemyError as e:
            print(e);
    def get_precursorFormulaAndMass_experimentIDAndTimePointAndSampleNameAbbreviationAndScanTypeAndReplicateAndMetID_peakSpectrum(self,experiment_id_I,time_point_I,sample_name_abbreviation_I,scan_type_I,sample_replicate_I,met_id_I):
        '''Querry met_ids that are used for the experiment        
        by time-point, sample name abbreviation, scan type, replicate numbers, and met_ids'''
        try:
            component_names = self.session.query(data_stage01_isotopomer_peakSpectrum.precursor_formula,
                    data_stage01_isotopomer_peakSpectrum.precursor_mass).filter(
                    data_stage01_isotopomer_peakSpectrum.met_id.like(met_id_I),
                    data_stage01_isotopomer_peakSpectrum.sample_name_abbreviation.like(sample_name_abbreviation_I),
                    data_stage01_isotopomer_peakSpectrum.time_point.like(time_point_I),
                    data_stage01_isotopomer_peakSpectrum.scan_type.like(scan_type_I),
                    data_stage01_isotopomer_peakSpectrum.experiment_id.like(experiment_id_I),
                    data_stage01_isotopomer_peakSpectrum.replicate_number == sample_replicate_I,
                    data_stage01_isotopomer_peakSpectrum.used_).group_by(
                    data_stage01_isotopomer_peakSpectrum.precursor_formula,
                    data_stage01_isotopomer_peakSpectrum.precursor_mass).order_by(
                    data_stage01_isotopomer_peakSpectrum.precursor_mass.asc(),
                    data_stage01_isotopomer_peakSpectrum.precursor_formula).all();
            precursor_formulas_O = [];
            precursor_mass_O = [];
            if not component_names:
                print('no precursor formula nor precursor mass found for experiment_id\ttime_point\tsample_name_abbreviation\tscan_type\tsample_replicate\tmet id');
                print((experiment_id_I + '\t'+ time_point_I + '\t'+ sample_name_abbreviation_I + '\t'+ scan_type_I + '\t'+ str(sample_replicate_I) + '\t'+ met_id_I));
            else:
                for cn in component_names:
                    precursor_formulas_O.append(cn.precursor_formula);
                    precursor_mass_O.append(cn.precursor_mass);
            return precursor_formulas_O, precursor_mass_O;
        except SQLAlchemyError as e:
            print(e);
    def get_precursorFormulaAndMass_experimentIDAndSampleNameAndMetIDAndScanType_peakSpectrum(self,experiment_id_I,sample_name_I,met_id_I,scan_type_I):
        '''Querry precursor formulas and masses that are used for the experiment'''
        try:
            component_names = self.session.query(data_stage01_isotopomer_peakSpectrum.precursor_formula,
                    data_stage01_isotopomer_peakSpectrum.precursor_mass).filter(
                    data_stage01_isotopomer_peakSpectrum.met_id.like(met_id_I),
                    data_stage01_isotopomer_peakSpectrum.sample_name.like(sample_name_I),
                    data_stage01_isotopomer_peakSpectrum.experiment_id.like(experiment_id_I),
                    data_stage01_isotopomer_peakSpectrum.scan_type.like(scan_type_I)).group_by(
                    data_stage01_isotopomer_peakSpectrum.precursor_formula,
                    data_stage01_isotopomer_peakSpectrum.precursor_mass).order_by(
                    data_stage01_isotopomer_peakSpectrum.precursor_mass.asc(),
                    data_stage01_isotopomer_peakSpectrum.precursor_formula).all();
            precursor_formulas_O = [];
            precursor_mass_O = [];
            if not component_names: exit('bad query result: get_precursorFormulaAndMass_experimentIDAndSampleNameAndScanType_peakSpectrum');
            for cn in component_names:
                precursor_formulas_O.append(cn.precursor_formula);
                precursor_mass_O.append(cn.precursor_mass);
            return precursor_formulas_O, precursor_mass_O;
        except SQLAlchemyError as e:
            print(e);
    # query scan types for data_stage01_peakSpectrum
    def get_scanType_experimentIDAndTimePointSampleNameAbbreviation_peakSpectrum(self,experiment_id_I,time_point_I,sample_name_abbreviation_I):
        '''Querry scan type that are used for the experiment by time-point and sample name abbreviation'''
        try:
            scantypes = self.session.query(data_stage01_isotopomer_peakSpectrum.scan_type).filter(
                    data_stage01_isotopomer_peakSpectrum.time_point.like(time_point_I),
                    data_stage01_isotopomer_peakSpectrum.sample_name_abbreviation.like(sample_name_abbreviation_I),
                    data_stage01_isotopomer_peakSpectrum.experiment_id.like(experiment_id_I),
                    data_stage01_isotopomer_peakSpectrum.used_).group_by(
                    data_stage01_isotopomer_peakSpectrum.scan_type).order_by(
                    data_stage01_isotopomer_peakSpectrum.scan_type.asc()).all();
            scan_type_O = [];
            if not scantypes:
                print('no scan types found for experiment_id\ttime_point\tsample_name_abbreviation');
                print((experiment_id_I + '\t'+ time_point_I + '\t'+ sample_name_abbreviation_I));
            else:
                for st in scantypes:
                    scan_type_O.append(st[0]);
            return scan_type_O;
        except SQLAlchemyError as e:
            print(e);
    def get_scanType_experimentIDAndSampleName_peakSpectrum(self,experiment_id_I,sample_name_I):
        '''Querry scan type that are used for the experiment'''
        try:
            component_names = self.session.query(data_stage01_isotopomer_peakSpectrum.scan_type).filter(
                    data_stage01_isotopomer_peakSpectrum.sample_name.like(sample_name_I),
                    data_stage01_isotopomer_peakSpectrum.experiment_id.like(experiment_id_I)).group_by(
                    data_stage01_isotopomer_peakSpectrum.scan_type).order_by(
                    data_stage01_isotopomer_peakSpectrum.scan_type.asc()).all();
            scan_type_O = [];
            if not component_names: exit('bad query result: get_metIDAndPrecursorFormula_experimentIDAndSampleName_peakSpectrum');
            for cn in component_names:
                scan_type_O.append(cn[0]);
            return scan_type_O;
        except SQLAlchemyError as e:
            print(e);
    # query replicate numbers for data_stage01_peakSpectrum
    def get_replicateNumber_experimentIDAndTimePointAndSampleNameAbbreviationAndScanType_peakSpectrum(self,experiment_id_I,time_point_I,sample_name_abbreviation_I,scan_type_I):
        '''Querry replicate numbers from the experiment
        by time-point, sample name abbreviation and scan type'''
        try:
            replicates = self.session.query(data_stage01_isotopomer_peakSpectrum.replicate_number).filter(
                    data_stage01_isotopomer_peakSpectrum.sample_name_abbreviation.like(sample_name_abbreviation_I),
                    data_stage01_isotopomer_peakSpectrum.time_point.like(time_point_I),
                    data_stage01_isotopomer_peakSpectrum.scan_type.like(scan_type_I),
                    data_stage01_isotopomer_peakSpectrum.experiment_id.like(experiment_id_I),
                    data_stage01_isotopomer_peakSpectrum.used_).group_by(
                    data_stage01_isotopomer_peakSpectrum.replicate_number).order_by(
                    data_stage01_isotopomer_peakSpectrum.replicate_number.asc()).all();
            sample_replicates_O = [];
            if not replicates: 
                print('no replicates found for experiment_id\ttime_point\tsample_name_abbreviation\tscan_type');
                print((experiment_id_I + '\t'+ time_point_I + '\t'+ sample_name_abbreviation_I + '\t'+ scan_type_I));
            else:
                for r in replicates:
                    sample_replicates_O.append(r[0]);
            return sample_replicates_O;
        except SQLAlchemyError as e:
            print(e);
    # query product formulas
    def get_productFormulas_experimentIDAndTimePointAndSampleNameAbbreviationAndScanTypeAndReplicateAndMetIDAndPrecursorFormula_peakSpectrum(self,experiment_id_I,time_point_I,sample_name_abbreviation_I,scan_type_I,sample_replicate_I,met_id_I,precursor_formula_I):
        '''Querry product formulas that are used for the experiment        
        by time-point, sample name abbreviation, scan type, replicate numbers, met_ids, and precursor formula'''
        try:
            data = self.session.query(data_stage01_isotopomer_peakSpectrum.product_formula).filter(
                    data_stage01_isotopomer_peakSpectrum.precursor_formula.like(precursor_formula_I),
                    data_stage01_isotopomer_peakSpectrum.met_id.like(met_id_I),
                    data_stage01_isotopomer_peakSpectrum.sample_name_abbreviation.like(sample_name_abbreviation_I),
                    data_stage01_isotopomer_peakSpectrum.time_point.like(time_point_I),
                    data_stage01_isotopomer_peakSpectrum.scan_type.like(scan_type_I),
                    data_stage01_isotopomer_peakSpectrum.experiment_id.like(experiment_id_I),
                    data_stage01_isotopomer_peakSpectrum.replicate_number == sample_replicate_I,
                    data_stage01_isotopomer_peakSpectrum.used_).group_by(
                    data_stage01_isotopomer_peakSpectrum.product_formula).order_by(
                    data_stage01_isotopomer_peakSpectrum.product_formula.asc()).all();
            product_formulas_O = [];
            if not data:
                print('no product formulas found for experiment_id\ttime_point\tsample_name_abbreviation\tscan_type\tsample_replicate\tmet id\tprecursor formula');
                print((experiment_id_I + '\t'+ time_point_I + '\t'+ sample_name_abbreviation_I + '\t'+ scan_type_I + '\t'+ str(sample_replicate_I) + '\t'+ met_id_I + '\t'+ precursor_formula_I));
            else:
                for d in data:
                    product_formulas_O.append(d.product_formula);
            return product_formulas_O;
        except SQLAlchemyError as e:
            print(e);
    def get_productFormulas_experimentIDAndSampleNameAndMetIDAndPrecursorFormulaAndScanType_peakSpectrum(self,experiment_id_I,sample_name_I,met_id_I,precursor_formula_I,scan_type_I):
        '''Querry peak data for a specific experiment_id, sample_name, met_id, and precursor_formula'''
        try:
            data = self.session.query(data_stage01_isotopomer_peakSpectrum.product_formula).filter(
                    data_stage01_isotopomer_peakSpectrum.sample_name.like(sample_name_I),
                    data_stage01_isotopomer_peakSpectrum.experiment_id.like(experiment_id_I),
                    data_stage01_isotopomer_peakSpectrum.met_id.like(met_id_I),
                    data_stage01_isotopomer_peakSpectrum.precursor_formula.like(precursor_formula_I),
                    data_stage01_isotopomer_peakSpectrum.scan_type.like(scan_type_I),
                    data_stage01_isotopomer_peakSpectrum.used_).group_by(
                    data_stage01_isotopomer_peakSpectrum.product_formula).order_by(
                    data_stage01_isotopomer_peakSpectrum.product_formula.asc()).all();
            product_formulas_O = [];
            if not data:
                print(('No product formulas found for sample_name: ' + sample_name_I + ', met_id: ' + met_id_I + ', and precursor_formula: ' + precursor_formula_I));
                return product_formulas_O;
            else:
                for d in data:
                    product_formulas_O.append(d.product_formula);
                return product_formulas_O;
        except SQLAlchemyError as e:
            print(e);
    # query normalized intensity from data_stage01_isotopomer_peakSpectrum
    def get_normalizedIntensity_experimentIDAndSampleAbbreviationAndTimePointAndReplicateNumberAndMetIDAndPrecursorFormulaAndMassAndScanType_peakSpectrum(self,experiment_id_I,sample_name_abbreviation_I,time_point_I,replicate_number_I,met_id_I,precursor_formula_I,precursor_mass_I,scan_type_I):
        '''Querry peak data for a specific experiment_id, sample_name, met_id, and scan type'''
        try:
            data = self.session.query(data_stage01_isotopomer_peakSpectrum.intensity_normalized,
                    data_stage01_isotopomer_peakSpectrum.intensity_normalized_units).filter(
                    data_stage01_isotopomer_peakSpectrum.sample_name_abbreviation.like(sample_name_abbreviation_I),
                    data_stage01_isotopomer_peakSpectrum.time_point.like(time_point_I),
                    data_stage01_isotopomer_peakSpectrum.precursor_formula.like(precursor_formula_I),
                    data_stage01_isotopomer_peakSpectrum.precursor_mass == precursor_mass_I,
                    data_stage01_isotopomer_peakSpectrum.experiment_id.like(experiment_id_I),
                    data_stage01_isotopomer_peakSpectrum.met_id.like(met_id_I),
                    data_stage01_isotopomer_peakSpectrum.scan_type.like(scan_type_I),
                    data_stage01_isotopomer_peakSpectrum.replicate_number == replicate_number_I,
                    data_stage01_isotopomer_peakSpectrum.used_).all();
            intensity_normalized_O = None;
            intensity_normalized_units_O = None;
            if not data:
                print(('No normalized intensities found for sample_name_abbreviation: ' + sample_name_abbreviation_I + ', met_id: ' + met_id_I + ', precursor_formula: ' + precursor_formula_I + ', precursor_mass: ' + str(precursor_mass_I)));
                return intensity_normalized_O;
            else:
                intensity_normalized_O = data[0][0];
                intensity_normalized_units_O = data[0][1];
                return intensity_normalized_O;
        except SQLAlchemyError as e:
            print(e);
    # query data from data_stage01_isotopomer_peakSpectrum
    def get_data_experimentIDAndTimePointAndSampleNameAbbreviationAndScanTypeAndReplicateAndMetIDAndPrecursorFormula_peakSpectrum(self,experiment_id_I,time_point_I,sample_name_abbreviation_I,scan_type_I,sample_replicate_I,met_id_I,precursor_formula_I):
        '''Querry data that are used for the experiment        
        by time-point, sample name abbreviation, scan type, replicate numbers, met_ids, and precursor formula'''

        try:
            data = self.session.query(data_stage01_isotopomer_peakSpectrum.product_formula,
                    data_stage01_isotopomer_peakSpectrum.product_mass,
                    data_stage01_isotopomer_peakSpectrum.intensity_normalized,
                    data_stage01_isotopomer_peakSpectrum.intensity_normalized_units).filter(
                    data_stage01_isotopomer_peakSpectrum.precursor_formula.like(precursor_formula_I),
                    data_stage01_isotopomer_peakSpectrum.met_id.like(met_id_I),
                    data_stage01_isotopomer_peakSpectrum.sample_name_abbreviation.like(sample_name_abbreviation_I),
                    data_stage01_isotopomer_peakSpectrum.time_point.like(time_point_I),
                    data_stage01_isotopomer_peakSpectrum.scan_type.like(scan_type_I),
                    data_stage01_isotopomer_peakSpectrum.experiment_id.like(experiment_id_I),
                    data_stage01_isotopomer_peakSpectrum.replicate_number == sample_replicate_I,
                    data_stage01_isotopomer_peakSpectrum.used_).order_by(
                    data_stage01_isotopomer_peakSpectrum.product_formula.asc(),
                    data_stage01_isotopomer_peakSpectrum.product_mass.asc()).all();
            product_formula = '';
            product_formula_old = '';
            data_O = {};
            mass_O = {};
            if not data:
                print(('No normalized intensities found for sample_name: ' + sample_name_I + ', met_id: ' + met_id_I + ', and precursor_formula: ' + precursor_formula_I));
                return data_O;
            else:
                for i,d in enumerate(data):
                    if i==0:
                        product_formula_old = d.product_formula;
                        mass_O[d.product_mass] = d.intensity_normalized;
                    product_formula = d.product_formula;
                    if product_formula != product_formula_old:
                        data_O[product_formula_old] = mass_O;
                        product_formula_old = product_formula
                        mass_O = {};
                        mass_O[d.product_mass] = d.intensity_normalized;
                    elif i == len(data)-1 and product_formula == product_formula_old:
                        mass_O[d.product_mass] = d.intensity_normalized;
                        data_O[product_formula] = mass_O;
                    else: mass_O[d.product_mass] = d.intensity_normalized;
                return data_O;
        except SQLAlchemyError as e:
            print(e);
    def get_normalizedIntensity_experimentIDAndSampleNameAndMetIDAndPrecursorFormulaAndScanType_peakSpectrum(self,experiment_id_I,sample_name_I,met_id_I,precursor_formula_I,scan_type_I):
        '''Querry peak data for a specific experiment_id, sample_name, met_id, and precursor_formula'''

        # possible duplicate of get_data_experimentIDAndSampleNameAndMetIDAndPrecursorFormulaAndScanType_peakSpectrum

        try:
            data = self.session.query(data_stage01_isotopomer_peakSpectrum.product_formula,
                    data_stage01_isotopomer_peakSpectrum.product_mass,
                    data_stage01_isotopomer_peakSpectrum.intensity_normalized,
                    data_stage01_isotopomer_peakSpectrum.intensity_normalized_units).filter(
                    data_stage01_isotopomer_peakSpectrum.sample_name.like(sample_name_I),
                    data_stage01_isotopomer_peakSpectrum.experiment_id.like(experiment_id_I),
                    data_stage01_isotopomer_peakSpectrum.met_id.like(met_id_I),
                    data_stage01_isotopomer_peakSpectrum.precursor_formula.like(precursor_formula_I),
                    data_stage01_isotopomer_peakSpectrum.scan_type.like(scan_type_I),
                    data_stage01_isotopomer_peakSpectrum.used_).order_by(
                    data_stage01_isotopomer_peakSpectrum.product_formula.asc(),
                    data_stage01_isotopomer_peakSpectrum.product_mass.asc()).all();
            product_formula = '';
            product_formula_old = '';
            data_O = {};
            mass_O = {};
            if not data:
                print(('No normalized intensities found for sample_name: ' + sample_name_I + ', met_id: ' + met_id_I + ', and precursor_formula: ' + precursor_formula_I));
                return data_O;
            else:
                for i,d in enumerate(data):
                    if i==0:
                        product_formula_old = d.product_formula;
                        mass_O[d.product_mass] = d.intensity_normalized;
                    product_formula = d.product_formula;
                    if product_formula != product_formula_old:
                        data_O[product_formula_old] = mass_O;
                        product_formula_old = product_formula
                        mass_O = {};
                        mass_O[d.product_mass] = d.intensity_normalized;
                    elif i == len(data)-1 and product_formula == product_formula_old:
                        mass_O[d.product_mass] = d.intensity_normalized;
                        data_O[product_formula] = mass_O;
                    else: mass_O[d.product_mass] = d.intensity_normalized;
                return data_O;
        except SQLAlchemyError as e:
            print(e);
    def get_data_experimentIDAndSampleNameAndMetIDAndPrecursorFormulaAndScanType_peakSpectrum(self,experiment_id_I,sample_name_I,met_id_I,precursor_formula_I,scan_type_I):
        '''Querry peak data for a specific experiment_id, sample_name, met_id, and precursor_formula'''
        try:
            data = self.session.query(data_stage01_isotopomer_peakSpectrum.product_formula,
                    data_stage01_isotopomer_peakSpectrum.product_mass,
                    data_stage01_isotopomer_peakSpectrum.intensity_corrected,
                    data_stage01_isotopomer_peakSpectrum.intensity_corrected_units).filter(
                    data_stage01_isotopomer_peakSpectrum.sample_name.like(sample_name_I),
                    data_stage01_isotopomer_peakSpectrum.experiment_id.like(experiment_id_I),
                    data_stage01_isotopomer_peakSpectrum.met_id.like(met_id_I),
                    data_stage01_isotopomer_peakSpectrum.precursor_formula.like(precursor_formula_I),
                    data_stage01_isotopomer_peakSpectrum.scan_type.like(scan_type_I),
                    data_stage01_isotopomer_peakSpectrum.used_).order_by(
                    data_stage01_isotopomer_peakSpectrum.product_formula.asc(),
                    data_stage01_isotopomer_peakSpectrum.product_mass.asc()).all();
            product_formula = '';
            product_formula_old = '';
            data_O = {};
            mass_O = {};
            if not data:
                print(('No data found for sample_name: ' + sample_name_I + ', met_id: ' + met_id_I + ', and precursor_formula: ' + precursor_formula_I));
                return data_O;
            else:
                for i,d in enumerate(data):
                    if i==0:
                        product_formula_old = d.product_formula;
                        mass_O[d.product_mass] = d.intensity_corrected;
                    product_formula = d.product_formula;
                    if product_formula != product_formula_old:
                        data_O[product_formula_old] = mass_O;
                        product_formula_old = product_formula
                        mass_O = {};
                        mass_O[d.product_mass] = d.intensity_corrected;
                    elif i == len(data)-1 and product_formula == product_formula_old:
                        mass_O[d.product_mass] = d.intensity_corrected;
                        data_O[product_formula] = mass_O;
                    else: mass_O[d.product_mass] = d.intensity_corrected;
                return data_O;
        except SQLAlchemyError as e:
            print(e);
    # update data for data_stage01_isotopomer_peakSpectrum
    def update_data_stage01_isotopomer_peakSpectrum(self,dataListUpdated_I):
        # update the data_stage01_isotopomer_peakSpectrum
        updates = [];
        for d in dataListUpdated_I:
            try:
                data_update = self.session.query(data_stage01_isotopomer_peakSpectrum).filter(
                        data_stage01_isotopomer_peakSpectrum.experiment_id.like(d['experiment_id']),
                        data_stage01_isotopomer_peakSpectrum.sample_name_abbreviation.like(d['sample_name_abbreviation']),
                        data_stage01_isotopomer_peakSpectrum.time_point.like(d['time_point']),
                        data_stage01_isotopomer_peakSpectrum.sample_type.like(d['sample_type']),
                        data_stage01_isotopomer_peakSpectrum.replicate_number == d['replicate_number'],
                        data_stage01_isotopomer_peakSpectrum.met_id.like(d['met_id']),
                        data_stage01_isotopomer_peakSpectrum.precursor_formula.like(d['precursor_formula']),
                        data_stage01_isotopomer_peakSpectrum.precursor_mass == d['precursor_mass'],
                        data_stage01_isotopomer_peakSpectrum.product_formula.like(d['product_formula']),
                        data_stage01_isotopomer_peakSpectrum.product_mass == d['product_mass'],
                        data_stage01_isotopomer_peakSpectrum.scan_type.like(d['scan_type'])).update(		
                        {
                        # 'intensity':d['intensity'],
                        #'intensity_units':d['intensity_units'],
                        'intensity_corrected':d['intensity_corrected'],
                        'intensity_corrected_units':d['intensity_corrected_units'],
                        'intensity_normalized':d['intensity_normalized'],
                        'intensity_normalized_units':d['intensity_normalized_units'],
                        'intensity_theoretical':d['intensity_theoretical'],
                        'abs_devFromTheoretical':d['abs_devFromTheoretical']},
                        synchronize_session=False);
                if data_update == 0:
                    print('row not found.')
                    print(d)
                    #print 'row will be added.'
                    #row = data_stage01_isotopomer_peakSpectrum(d['experiment_id'],
                    #    d['sample_name'],
                    #    d['sample_name_abbreviation'],
                    #    d['sample_type'],
                    #    d['time_point'],
                    #    d['replicate_number'],
                    #    d['met_id'],
                    #    d['precursor_formula'],
                    #    d['precursor_mass'],
                    #    d['product_formula'],
                    #    d['product_mass'],
                    #    0.0,
                    #    'cps',
                    #    d['intensity_corrected'],
                    #    d['intensity_corrected_units'],
                    #    d['intensity_normalized'],
                    #    d['intensity_normalized_units'],
                    #    d['intensity_theoretical'],
                    #    d['abs_devFromTheoretical'],
                    #    d['scan_type'],
                    #    True,
                    #    None);
                    #self.session.add(row);
                    #self.session.commit();
                #elif data_update ==1:
                #    print 'good update'
                updates.append(data_update);
            except SQLAlchemyError as e:
                print(e);
        self.session.commit();
    def update_validFragments_stage01_isotopomer_peakSpectrum(self,dataListUpdated_I):
        # update the data_stage01_isotopomer_peakSpectrum
        updates = [];
        # set 'used_' = False for all met/fragment pairs for the experiment
        try:
            data_update = self.session.query(data_stage01_isotopomer_peakSpectrum).filter(
                        data_stage01_isotopomer_peakSpectrum.experiment_id.like(dataListUpdated_I[0]['experiment_id'])).update(		
                        {
                        'used_':False},
                        synchronize_session=False);
        except SQLAlchemyError as e:
            print(e);
        self.session.commit();
        # set 'used_' = True for falidated met/fragment pairs for the experiment
        for d in dataListUpdated_I:
            try:
                data_update = self.session.query(data_stage01_isotopomer_peakSpectrum).filter(
                        data_stage01_isotopomer_peakSpectrum.experiment_id.like(d['experiment_id']),
                        data_stage01_isotopomer_peakSpectrum.met_id.like(d['met_id']),
                        data_stage01_isotopomer_peakSpectrum.product_formula.like(d['product_formula'])).update(		
                        {
                        'used_':True},
                        synchronize_session=False);
                if data_update == 0:
                    print('row not found.')
                    print(d)
                updates.append(data_update);
            except SQLAlchemyError as e:
                print(e);
        self.session.commit();

    def add_dataStage01IsotopomerPeakSpectrum(self,data_I):
        '''add rows of data_stage01_isotopomer_peakSpectrum'''
        if data_I:
            #cnt = 0;
            for d in data_I:
                try:
                    data_add = data_stage01_isotopomer_peakSpectrum(d['experiment_id'],
                                    d['sample_name'],
                                    d['sample_name_abbreviation'],
                                    d['sample_type'],
                                    d['time_point'],
                                    d['replicate_number'],
                                    d['met_id'],
                                    d['precursor_formula'],
                                    d['precursor_mass'],
                                    d['product_formula'],
                                    d['product_mass'],
                                    d['intensity'],
                                    d['intensity_units'],
                                    d['intensity_corrected'],
                                    d['intensity_corrected_units'],
                                    d['intensity_normalized'],
                                    d['intensity_normalized_units'],
                                    d['intensity_theoretical'],
                                    d['abs_devFromTheoretical'],
                                    d['scan_type'],
                                    d['used_'],
                                    d['comment_']);
                    self.session.add(data_add);
                    #cnt = cnt + 1;
                    #if cnt > 1000: 
                    #    self.session.commit();
                    #    cnt = 0;
                except SQLAlchemyError as e:
                    print(e);
            self.session.commit();

    def update_dataStage01IsotopomerPeakSpectrum(self,dataListUpdated_I):
        # update the data_stage01_isotopomer_peakSpectrum
        for d in dataListUpdated_I:
            try:
                data_update = self.session.query(data_stage01_isotopomer_peakSpectrum).filter(
                        data_stage01_isotopomer_peakSpectrum.id == d['id']).update(
                        #data_stage01_isotopomer_peakSpectrum.experiment_id.like(d['experiment_id']),
                        #data_stage01_isotopomer_peakSpectrum.sample_name_abbreviation.like(d['sample_name_abbreviation']),
                        #data_stage01_isotopomer_peakSpectrum.time_point.like(d['time_point']),
                        #data_stage01_isotopomer_peakSpectrum.sample_type.like(d['sample_type']),
                        #data_stage01_isotopomer_peakSpectrum.replicate_number == d['replicate_number'],
                        #data_stage01_isotopomer_peakSpectrum.met_id.like(d['met_id']),
                        #data_stage01_isotopomer_peakSpectrum.precursor_formula.like(d['precursor_formula']),
                        #data_stage01_isotopomer_peakSpectrum.precursor_mass == d['precursor_mass'],
                        #data_stage01_isotopomer_peakSpectrum.product_formula.like(d['product_formula']),
                        #data_stage01_isotopomer_peakSpectrum.product_mass == d['product_mass']).update(		
                        {'intensity':d['intensity'],
                        'intensity_units':d['intensity_units'],
                        'intensity_corrected':d['intensity_corrected'],
                        'intensity_corrected_units':d['intensity_corrected_units'],
                        'intensity_normalized':d['intensity_normalized'],
                        'intensity_normalized_units':d['intensity_normalized_units'],
                        'scan_type':d['scan_type'],
                        'used_':d['used_'],
                        'comment_':d['comment_']},
                        synchronize_session=False);
                if data_update == 0:
                    print('row not found.')
                    print(d)
            except SQLAlchemyError as e:
                print(e);
        self.session.commit();