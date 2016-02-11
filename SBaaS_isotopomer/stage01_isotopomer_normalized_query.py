from .stage01_isotopomer_normalized_postgresql_models import *
from SBaaS_LIMS.lims_experiment_postgresql_models import *
from SBaaS_LIMS.lims_sample_postgresql_models import *

from SBaaS_base.sbaas_base_query_update import sbaas_base_query_update
from SBaaS_base.sbaas_base_query_drop import sbaas_base_query_drop
from SBaaS_base.sbaas_base_query_initialize import sbaas_base_query_initialize
from SBaaS_base.sbaas_base_query_insert import sbaas_base_query_insert
from SBaaS_base.sbaas_base_query_select import sbaas_base_query_select
from SBaaS_base.sbaas_base_query_delete import sbaas_base_query_delete

from SBaaS_base.sbaas_template_query import sbaas_template_query

class stage01_isotopomer_normalized_query(sbaas_template_query):
    def initialize_supportedTables(self):
        '''Set the supported tables dict for 
        '''
        tables_supported = {'data_stage01_isotopomer_normalized':data_stage01_isotopomer_normalized,
                        };
        self.set_supportedTables(tables_supported);
    def initialize_dataStage01_isotopomer_normalized(self):
        try:
            data_stage01_isotopomer_normalized.__table__.create(self.engine,True);
        except SQLAlchemyError as e:
            print(e);
    def drop_dataStage01_isotopomer_normalized(self):
        try:
            data_stage01_isotopomer_normalized.__table__.drop(self.engine,True);
        except SQLAlchemyError as e:
            print(e);
    def reset_dataStage01_isotopomer_normalized(self,experiment_id_I = None):
        try:
            if experiment_id_I:
                reset = self.session.query(data_stage01_isotopomer_normalized).filter(data_stage01_isotopomer_normalized.experiment_id.like(experiment_id_I)).delete(synchronize_session=False);
                self.session.commit();
        except SQLAlchemyError as e:
            print(e);
    # query sample names from data_stage01_isotopomer_normalized
    def get_sampleIDs_experimentID_dataStage01Normalized(self,experiment_id_I):
        '''Querry sample ids that are used from
        the experiment'''
        try:
            sample_ids = self.session.query(data_stage01_isotopomer_normalized.sample_id).filter(
                    data_stage01_isotopomer_normalized.experiment_id.like(experiment_id_I),
                    data_stage01_isotopomer_normalized.used_.is_(True)).group_by(
                    data_stage01_isotopomer_normalized.sample_id).order_by(
                    data_stage01_isotopomer_normalized.sample_id.asc()).all();
            sample_ids_O = [];
            for si in sample_ids: sample_ids_O.append(si.sample_id);
            return sample_ids_O;
        except SQLAlchemyError as e:
            print(e);
    def get_sampleNames_experimentID_dataStage01Normalized(self,experiment_id_I):
        '''Querry sample names (i.e. unknowns) that are used from
        the experiment'''
        try:
            sample_names = self.session.query(data_stage01_isotopomer_normalized.sample_name).filter(
                    data_stage01_isotopomer_normalized.experiment_id.like(experiment_id_I),
                    data_stage01_isotopomer_normalized.used_.is_(True)).group_by(
                    data_stage01_isotopomer_normalized.sample_name).order_by(
                    data_stage01_isotopomer_normalized.sample_name.asc()).all();
            sample_names_O = [];
            for sn in sample_names: sample_names_O.append(sn.sample_name);
            return sample_names_O;
        except SQLAlchemyError as e:
            print(e);
    def get_sampleNamesAndReplicateNumbersAndSampleTypes_experimentIDAndSampleNameAbbreviationAndMetIDAndTimePointAndDilutionAndScanType_dataStage01Normalized(\
        self,experiment_id_I,sample_name_abbreviation_I,met_id_I,time_point_I,sample_dilution_I, scan_type_I):
        '''Querry sample names that are used from
        the experiment'''
        try:
            sample_names = self.session.query(data_stage01_isotopomer_normalized.sample_name,
                    data_stage01_isotopomer_normalized.replicate_number,
                    data_stage01_isotopomer_normalized.sample_type).filter(
                    data_stage01_isotopomer_normalized.experiment_id.like(experiment_id_I),
                    data_stage01_isotopomer_normalized.sample_name_abbreviation.like(sample_name_abbreviation_I),
                    data_stage01_isotopomer_normalized.time_point.like(time_point_I),
                    data_stage01_isotopomer_normalized.met_id.like(met_id_I),
                    data_stage01_isotopomer_normalized.dilution == sample_dilution_I,
                    data_stage01_isotopomer_normalized.scan_type.like(scan_type_I),
                    data_stage01_isotopomer_normalized.used_.is_(True)).group_by(
                    data_stage01_isotopomer_normalized.sample_name,
                    data_stage01_isotopomer_normalized.replicate_number,
                    data_stage01_isotopomer_normalized.sample_type).order_by(
                    data_stage01_isotopomer_normalized.sample_name.asc()).all();
            sample_names_O = [];
            sample_replicates_O = [];
            sample_types_O = [];
            if not sample_names:
                print("no results found")
                print("experiment_id_I	sample_name_abbreviation_I	met_id_I	time_point_I	sample_dilution_I")
                print(experiment_id_I,sample_name_abbreviation_I,met_id_I,time_point_I,sample_dilution_I)
                return sample_names_O,sample_replicates_O,sample_types_O;
            else:
                for sn in sample_names:
                    sample_names_O.append(sn.sample_name);
                    sample_replicates_O.append(sn.replicate_number);
                    sample_types_O.append(sn.sample_type);
                return sample_names_O,sample_replicates_O,sample_types_O;
        except SQLAlchemyError as e:
            print(e);
    def get_sampleNamesAndReplicateNumbersAndSampleTypes_experimentIDAndSampleNameAbbreviationAndMetIDAndTimePointAndScanType_dataStage01Normalized(\
        self,experiment_id_I,sample_name_abbreviation_I,met_id_I,time_point_I, scan_type_I):
        '''Querry sample names that are used from
        the experiment'''
        try:
            sample_names = self.session.query(data_stage01_isotopomer_normalized.sample_name,
                    data_stage01_isotopomer_normalized.replicate_number,
                    data_stage01_isotopomer_normalized.sample_type).filter(
                    data_stage01_isotopomer_normalized.experiment_id.like(experiment_id_I),
                    data_stage01_isotopomer_normalized.sample_name_abbreviation.like(sample_name_abbreviation_I),
                    data_stage01_isotopomer_normalized.time_point.like(time_point_I),
                    data_stage01_isotopomer_normalized.met_id.like(met_id_I),
                    data_stage01_isotopomer_normalized.scan_type.like(scan_type_I),
                    data_stage01_isotopomer_normalized.used_.is_(True)).group_by(
                    data_stage01_isotopomer_normalized.sample_name,
                    data_stage01_isotopomer_normalized.replicate_number,
                    data_stage01_isotopomer_normalized.sample_type).order_by(
                    data_stage01_isotopomer_normalized.sample_name.asc()).all();
            sample_names_O = [];
            sample_replicates_O = [];
            sample_types_O = [];
            if not sample_names:
                print("no results found")
                print("experiment_id_I	sample_name_abbreviation_I	met_id_I	time_point_I	sample_dilution_I")
                print(experiment_id_I,sample_name_abbreviation_I,met_id_I,time_point_I)
                return sample_names_O,sample_replicates_O,sample_types_O;
            else:
                for sn in sample_names:
                    sample_names_O.append(sn.sample_name);
                    sample_replicates_O.append(sn.replicate_number);
                    sample_types_O.append(sn.sample_type);
                return sample_names_O,sample_replicates_O,sample_types_O;
        except SQLAlchemyError as e:
            print(e);
    def get_sampleNameShort_experimentIDAndSampleName_dataStage01Normalized(self,experiment_id_I,sample_name_I):
        '''Querry sample name short that are used from
        the experiment'''
        try:
            sample_name_short = self.session.query(sample_description.sample_name_short).filter(
                    sample.sample_name.like(sample_name_I),
                    data_stage01_isotopomer_normalized.experiment_id.like(experiment_id_I),
                    data_stage01_isotopomer_normalized.used_.is_(True),
                    data_stage01_isotopomer_normalized.sample_name.like(sample.sample_name),
                    sample.sample_id.like(sample_description.sample_id)).group_by(
                    sample_description.sample_name_short).all();
            sample_name_short_O = sample_name_short[0];
            return sample_name_short_O;
        except SQLAlchemyError as e:
            print(e);
    # query sample name abbreviations from data_stage01_isotopomer_normalized
    def get_sampleNameAbbreviations_experimentID_dataStage01Normalized(self,experiment_id_I):
        '''Querry sample names (i.e. unknowns) that are used from
        the experiment'''
        try:
            sample_names = self.session.query(sample_description.sample_name_abbreviation).filter(
                    data_stage01_isotopomer_normalized.experiment_id.like(experiment_id_I),
                    data_stage01_isotopomer_normalized.sample_name.like(sample.sample_name),
                    sample.sample_id.like(sample_description.sample_id),
                    data_stage01_isotopomer_normalized.used_.is_(True)).group_by(
                    sample_description.sample_name_abbreviation).order_by(
                    sample_description.sample_name_abbreviation.asc()).all();
            sample_names_O = [];
            for sn in sample_names: sample_names_O.append(sn.sample_name_abbreviation);
            return sample_names_O;
        except SQLAlchemyError as e:
            print(e);
    def get_sampleNameAbbreviations_experimentIDAndSampleTypeAndTimePointAndDilution_dataStage01Normalized(self,experiment_id_I,sample_type_I,time_point_I,dilution_I):
        '''Querry sample name abbreviations that are used from
        the experiment for specific time-points and dilutions'''
        try:
            sample_name_abbreviations = self.session.query(
                    data_stage01_isotopomer_normalized.sample_name_abbreviation).filter(
                    data_stage01_isotopomer_normalized.experiment_id.like(experiment_id_I),
                    data_stage01_isotopomer_normalized.used_.is_(True),
                    data_stage01_isotopomer_normalized.sample_type.like(sample_type_I),
                    data_stage01_isotopomer_normalized.dilution == dilution_I,
                    data_stage01_isotopomer_normalized.time_point.like(time_point_I)).group_by(
                    data_stage01_isotopomer_normalized.sample_name_abbreviation).order_by(
                    data_stage01_isotopomer_normalized.sample_name_abbreviation).all();
            sample_name_abbreviations_O = [];
            for sn in sample_name_abbreviations:
                sample_name_abbreviations_O.append(sn[0]);
            return sample_name_abbreviations_O;
        except SQLAlchemyError as e:
            print(e);
    def get_sampleNameAbbreviations_experimentIDAndSampleTypeAndTimePointAndDilutionAndSampleName_dataStage01Normalized(self,experiment_id_I,sample_type_I,time_point_I,dilution_I,sample_name_I):
        '''Querry sample name abbreviations that are used from
        the experiment for specific time-points and dilutions'''
        try:
            sample_name_abbreviations = self.session.query(
                    data_stage01_isotopomer_normalized.sample_name_abbreviation).filter(
                    data_stage01_isotopomer_normalized.experiment_id.like(experiment_id_I),
                    data_stage01_isotopomer_normalized.used_.is_(True),
                    data_stage01_isotopomer_normalized.sample_type.like(sample_type_I),
                    data_stage01_isotopomer_normalized.dilution == dilution_I,
                    data_stage01_isotopomer_normalized.time_point.like(time_point_I),
                    data_stage01_isotopomer_normalized.sample_name.like(sample_name_I)).group_by(
                    data_stage01_isotopomer_normalized.sample_name_abbreviation).order_by(
                    data_stage01_isotopomer_normalized.sample_name_abbreviation).all();
            sample_name_abbreviations_O = [];
            for sn in sample_name_abbreviations:
                sample_name_abbreviations_O.append(sn[0]);
            return sample_name_abbreviations_O;
        except SQLAlchemyError as e:
            print(e);
    def get_sampleNameAbbreviations_experimentIDAndSampleTypeAndTimePointAndComment_dataStage01Normalized(self,experiment_id_I,sample_type_I,time_point_I,comment_I):
        '''Querry sample name abbreviations that are used from
        the experiment for specific time-points'''
        try:
            sample_name_abbreviations = self.session.query(
                    data_stage01_isotopomer_normalized.sample_name_abbreviation).filter(
                    data_stage01_isotopomer_normalized.experiment_id.like(experiment_id_I),
                    data_stage01_isotopomer_normalized.comment_.like(comment_I),
                    data_stage01_isotopomer_normalized.used_.is_(True),
                    data_stage01_isotopomer_normalized.sample_type.like(sample_type_I),
                    data_stage01_isotopomer_normalized.time_point.like(time_point_I)).group_by(
                    data_stage01_isotopomer_normalized.sample_name_abbreviation).order_by(
                    data_stage01_isotopomer_normalized.sample_name_abbreviation).all();
            sample_name_abbreviations_O = [];
            for sn in sample_name_abbreviations:
                sample_name_abbreviations_O.append(sn[0]);
            return sample_name_abbreviations_O;
        except SQLAlchemyError as e:
            print(e);
    def get_sampleNameAbbreviations_experimentIDAndSampleTypeAndTimePoint_dataStage01Normalized(self,experiment_id_I,sample_type_I,time_point_I):
        '''Querry sample name abbreviations that are used from
        the experiment for specific time-points'''
        try:
            sample_name_abbreviations = self.session.query(
                    data_stage01_isotopomer_normalized.sample_name_abbreviation).filter(
                    data_stage01_isotopomer_normalized.experiment_id.like(experiment_id_I),
                    data_stage01_isotopomer_normalized.used_.is_(True),
                    data_stage01_isotopomer_normalized.sample_type.like(sample_type_I),
                    data_stage01_isotopomer_normalized.time_point.like(time_point_I)).group_by(
                    data_stage01_isotopomer_normalized.sample_name_abbreviation).order_by(
                    data_stage01_isotopomer_normalized.sample_name_abbreviation).all();
            sample_name_abbreviations_O = [];
            for sn in sample_name_abbreviations:
                sample_name_abbreviations_O.append(sn[0]);
            return sample_name_abbreviations_O;
        except SQLAlchemyError as e:
            print(e);
    def get_sampleNameAbbreviations_experimentIDAndSampleTypeAndTimePointAndSampleNameAndComment_dataStage01Normalized(self,experiment_id_I,sample_type_I,time_point_I,sample_name_I,comment_I):
        '''Querry sample name abbreviations that are used from
        the experiment for specific time-points'''
        try:
            sample_name_abbreviations = self.session.query(
                    data_stage01_isotopomer_normalized.sample_name_abbreviation).filter(
                    data_stage01_isotopomer_normalized.experiment_id.like(experiment_id_I),
                    data_stage01_isotopomer_normalized.comment_.like(comment_I),
                    data_stage01_isotopomer_normalized.used_.is_(True),
                    data_stage01_isotopomer_normalized.sample_type.like(sample_type_I),
                    data_stage01_isotopomer_normalized.time_point.like(time_point_I),
                    data_stage01_isotopomer_normalized.sample_name.like(sample_name_I)).group_by(
                    data_stage01_isotopomer_normalized.sample_name_abbreviation).order_by(
                    data_stage01_isotopomer_normalized.sample_name_abbreviation).all();
            sample_name_abbreviations_O = [];
            for sn in sample_name_abbreviations:
                sample_name_abbreviations_O.append(sn[0]);
            return sample_name_abbreviations_O;
        except SQLAlchemyError as e:
            print(e);
    def get_sampleNameAbbreviations_experimentIDAndSampleTypeAndTimePointAndSampleName_dataStage01Normalized(self,experiment_id_I,sample_type_I,time_point_I,sample_name_I):
        '''Querry sample name abbreviations that are used from
        the experiment for specific time-points'''
        try:
            sample_name_abbreviations = self.session.query(
                    data_stage01_isotopomer_normalized.sample_name_abbreviation).filter(
                    data_stage01_isotopomer_normalized.experiment_id.like(experiment_id_I),
                    data_stage01_isotopomer_normalized.used_.is_(True),
                    data_stage01_isotopomer_normalized.sample_type.like(sample_type_I),
                    data_stage01_isotopomer_normalized.time_point.like(time_point_I),
                    data_stage01_isotopomer_normalized.sample_name.like(sample_name_I)).group_by(
                    data_stage01_isotopomer_normalized.sample_name_abbreviation).order_by(
                    data_stage01_isotopomer_normalized.sample_name_abbreviation).all();
            sample_name_abbreviations_O = [];
            for sn in sample_name_abbreviations:
                sample_name_abbreviations_O.append(sn[0]);
            return sample_name_abbreviations_O;
        except SQLAlchemyError as e:
            print(e);
    def get_sampleNameAbbreviations_experimentIDAndSampleTypeAndTimePointAndSampleNameAbbreviation_dataStage01Normalized(self,experiment_id_I,sample_type_I,time_point_I,sample_name_abbreviation_I,exp_type_I=5):
        '''Querry sample name abbreviations that are used from
        the experiment for specific time-points'''
        try:
            sample_name_abbreviations = self.session.query(
                    data_stage01_isotopomer_normalized.sample_name_abbreviation).filter(
                    sample_description.sample_name_abbreviation.like(sample_name_abbreviation_I),
                    experiment.id.like(experiment_id_I),
                    experiment.exp_type_id == exp_type_I,
                    sample.sample_id.like(sample_description.sample_id),
                    experiment.sample_name.like(sample.sample_name),
                    data_stage01_isotopomer_normalized.experiment_id.like(experiment_id_I),
                    data_stage01_isotopomer_normalized.used_.is_(True),
                    data_stage01_isotopomer_normalized.sample_type.like(sample_type_I),
                    data_stage01_isotopomer_normalized.time_point.like(time_point_I),
                    data_stage01_isotopomer_normalized.sample_name.like(sample.sample_name)).group_by(
                    data_stage01_isotopomer_normalized.sample_name_abbreviation).order_by(
                    data_stage01_isotopomer_normalized.sample_name_abbreviation).all();
            sample_name_abbreviations_O = [];
            for sn in sample_name_abbreviations:
                sample_name_abbreviations_O.append(sn[0]);
            return sample_name_abbreviations_O;
        except SQLAlchemyError as e:
            print(e);
    # Query scan types from data_stage01_normalized
    def get_scanTypes_experimentIDAndTimePointAndDilutionAndSampleAbbreviations_dataStage01Normalized(self,experiment_id_I,time_point_I,dilution_I,sample_name_abbreviations_I):
        '''Querry scan types that are used from the experiment for specific time-points and dilutions and sample name abbreviations'''
        try:
            scan_types = self.session.query(
                    data_stage01_isotopomer_normalized.scan_type).filter(
                    data_stage01_isotopomer_normalized.experiment_id.like(experiment_id_I),
                    data_stage01_isotopomer_normalized.used_.is_(True),
                    data_stage01_isotopomer_normalized.dilution == dilution_I,
                    data_stage01_isotopomer_normalized.time_point.like(time_point_I),
                    data_stage01_isotopomer_normalized.sample_name_abbreviation.like(sample_name_abbreviations_I)).group_by(
                    data_stage01_isotopomer_normalized.scan_type).order_by(
                    data_stage01_isotopomer_normalized.scan_type).all();
            scan_types_O = [];
            for st in scan_types:
                scan_types_O.append(st[0]);
            return scan_types_O;
        except SQLAlchemyError as e:
            print(e);
    def get_scanTypes_experimentIDAndTimePointAndSampleAbbreviationsAndComment_dataStage01Normalized(self,experiment_id_I,time_point_I,sample_name_abbreviations_I,comment_I):
        '''Querry scan types that are used from the experiment for specific time-points and sample name abbreviations'''
        try:
            scan_types = self.session.query(
                    data_stage01_isotopomer_normalized.scan_type).filter(
                    data_stage01_isotopomer_normalized.experiment_id.like(experiment_id_I),
                    data_stage01_isotopomer_normalized.comment_.like(comment_I),
                    data_stage01_isotopomer_normalized.used_.is_(True),
                    data_stage01_isotopomer_normalized.time_point.like(time_point_I),
                    data_stage01_isotopomer_normalized.sample_name_abbreviation.like(sample_name_abbreviations_I)).group_by(
                    data_stage01_isotopomer_normalized.scan_type).order_by(
                    data_stage01_isotopomer_normalized.scan_type).all();
            scan_types_O = [];
            for st in scan_types:
                scan_types_O.append(st[0]);
            return scan_types_O;
        except SQLAlchemyError as e:
            print(e);
    def get_scanTypes_experimentIDAndTimePointAndSampleAbbreviations_dataStage01Normalized(self,experiment_id_I,time_point_I,sample_name_abbreviations_I):
        '''Querry scan types that are used from the experiment for specific time-points and sample name abbreviations'''
        try:
            scan_types = self.session.query(
                    data_stage01_isotopomer_normalized.scan_type).filter(
                    data_stage01_isotopomer_normalized.experiment_id.like(experiment_id_I),
                    data_stage01_isotopomer_normalized.used_.is_(True),
                    data_stage01_isotopomer_normalized.time_point.like(time_point_I),
                    data_stage01_isotopomer_normalized.sample_name_abbreviation.like(sample_name_abbreviations_I)).group_by(
                    data_stage01_isotopomer_normalized.scan_type).order_by(
                    data_stage01_isotopomer_normalized.scan_type).all();
            scan_types_O = [];
            for st in scan_types:
                scan_types_O.append(st[0]);
            return scan_types_O;
        except SQLAlchemyError as e:
            print(e);
    def get_scanTypes_experimentIDAndTimePointAndSampleAbbreviationsAndSampleType_dataStage01Normalized(self,experiment_id_I,time_point_I,sample_name_abbreviations_I,sample_type_I):
        '''Querry scan types that are used from the experiment for specific time-points and sample name abbreviations'''
        try:
            scan_types = self.session.query(
                    data_stage01_isotopomer_normalized.scan_type).filter(
                    data_stage01_isotopomer_normalized.experiment_id.like(experiment_id_I),
                    data_stage01_isotopomer_normalized.used_.is_(True),
                    data_stage01_isotopomer_normalized.time_point.like(time_point_I),
                    data_stage01_isotopomer_normalized.sample_type.like(sample_type_I),
                    data_stage01_isotopomer_normalized.sample_name_abbreviation.like(sample_name_abbreviations_I)).group_by(
                    data_stage01_isotopomer_normalized.scan_type).order_by(
                    data_stage01_isotopomer_normalized.scan_type).all();
            scan_types_O = [];
            for st in scan_types:
                scan_types_O.append(st[0]);
            return scan_types_O;
        except SQLAlchemyError as e:
            print(e);
    def get_scanTypes_experimentIDAndSampleAbbreviations_dataStage01Normalized(self,experiment_id_I,sample_name_abbreviation_I):
        '''Querry scan types that are used from the experiment for specific sample names'''
        try:
            scan_types = self.session.query(
                    data_stage01_isotopomer_normalized.scan_type).filter(
                    data_stage01_isotopomer_normalized.experiment_id.like(experiment_id_I),
                    data_stage01_isotopomer_normalized.used_.is_(True),
                    data_stage01_isotopomer_normalized.sample_name_abbreviation.like(sample_name_abbreviation_I)).group_by(
                    data_stage01_isotopomer_normalized.scan_type).order_by(
                    data_stage01_isotopomer_normalized.scan_type).all();
            scan_types_O = [];
            for st in scan_types:
                scan_types_O.append(st[0]);
            return scan_types_O;
        except SQLAlchemyError as e:
            print(e);
    # query met ids from data_stage01_isotopomer_normalized
    def get_metIDs_experimentIDAndSampleAbbreviationAndTimePointAndDilutionAndScanType_dataStage01Normalized(self,experiment_id_I,sample_name_abbreviation_I,time_point_I,dilution_I,scan_type_I):
        '''Querry met ids that are used for the experiment, sample abbreviation, time point, dilution, scan type'''
        try:
            met_ids = self.session.query(data_stage01_isotopomer_normalized.met_id).filter(
                    data_stage01_isotopomer_normalized.sample_name_abbreviation.like(sample_name_abbreviation_I),
                    data_stage01_isotopomer_normalized.experiment_id.like(experiment_id_I),
                    data_stage01_isotopomer_normalized.time_point.like(time_point_I),
                    data_stage01_isotopomer_normalized.dilution == dilution_I,
                    data_stage01_isotopomer_normalized.scan_type.like(scan_type_I),
                    data_stage01_isotopomer_normalized.used_.is_(True)).group_by(
                    data_stage01_isotopomer_normalized.met_id).order_by(
                    data_stage01_isotopomer_normalized.met_id.asc()).all();
            met_ids_O = [];
            if not(met_ids):
                print("no results found")
                print("experiment_id_I	sample_name_abbreviation_I	time_point_I	dilution_I	scan_type_I");
                print(experiment_id_I,sample_name_abbreviation_I,time_point_I,dilution_I,scan_type_I);
            else:
                for cn in met_ids:
                    met_ids_O.append(cn[0]);
                return met_ids_O;
        except SQLAlchemyError as e:
            print(e);
    def get_metIDs_experimentIDAndSampleAbbreviationAndTimePointAndScanTypeAndComment_dataStage01Normalized(self,experiment_id_I,sample_name_abbreviation_I,time_point_I,scan_type_I,comment_I):
        '''Querry met ids that are used for the experiment, sample abbreviation, time point, scan type'''
        try:
            met_ids = self.session.query(data_stage01_isotopomer_normalized.met_id).filter(
                    data_stage01_isotopomer_normalized.sample_name_abbreviation.like(sample_name_abbreviation_I),
                    data_stage01_isotopomer_normalized.comment_.like(comment_I),
                    data_stage01_isotopomer_normalized.experiment_id.like(experiment_id_I),
                    data_stage01_isotopomer_normalized.time_point.like(time_point_I),
                    data_stage01_isotopomer_normalized.scan_type.like(scan_type_I),
                    data_stage01_isotopomer_normalized.used_.is_(True)).group_by(
                    data_stage01_isotopomer_normalized.met_id).order_by(
                    data_stage01_isotopomer_normalized.met_id.asc()).all();
            met_ids_O = [];
            if not(met_ids):
                print("no results found")
                print("experiment_id_I	sample_name_abbreviation_I	time_point_I	scan_type_I comment_I");
                print(experiment_id_I,sample_name_abbreviation_I,time_point_I,scan_type_I,comment_I);
            else:
                for cn in met_ids:
                    met_ids_O.append(cn[0]);
                return met_ids_O;
        except SQLAlchemyError as e:
            print(e);
    def get_metIDs_experimentIDAndSampleAbbreviationAndTimePointAndScanType_dataStage01Normalized(self,experiment_id_I,sample_name_abbreviation_I,time_point_I,scan_type_I):
        '''Querry met ids that are used for the experiment, sample abbreviation, time point, scan type'''
        try:
            met_ids = self.session.query(data_stage01_isotopomer_normalized.met_id).filter(
                    data_stage01_isotopomer_normalized.sample_name_abbreviation.like(sample_name_abbreviation_I),
                    data_stage01_isotopomer_normalized.experiment_id.like(experiment_id_I),
                    data_stage01_isotopomer_normalized.time_point.like(time_point_I),
                    data_stage01_isotopomer_normalized.scan_type.like(scan_type_I),
                    data_stage01_isotopomer_normalized.used_.is_(True)).group_by(
                    data_stage01_isotopomer_normalized.met_id).order_by(
                    data_stage01_isotopomer_normalized.met_id.asc()).all();
            met_ids_O = [];
            if not(met_ids):
                print("no results found")
                print("experiment_id_I	sample_name_abbreviation_I	time_point_I	scan_type_I");
                print(experiment_id_I,sample_name_abbreviation_I,time_point_I,scan_type_I);
            else:
                for cn in met_ids:
                    met_ids_O.append(cn[0]);
                return met_ids_O;
        except SQLAlchemyError as e:
            print(e);
    def get_metIDs_experimentIDAndSampleAbbreviationAndTimePointAndSampleTypeAndScanType_dataStage01Normalized(self,experiment_id_I,sample_name_abbreviation_I,time_point_I,sample_type_I,scan_type_I):
        '''Querry met ids that are used for the experiment, sample abbreviation, time point, scan type'''
        try:
            met_ids = self.session.query(data_stage01_isotopomer_normalized.met_id).filter(
                    data_stage01_isotopomer_normalized.sample_name_abbreviation.like(sample_name_abbreviation_I),
                    data_stage01_isotopomer_normalized.experiment_id.like(experiment_id_I),
                    data_stage01_isotopomer_normalized.time_point.like(time_point_I),
                    data_stage01_isotopomer_normalized.sample_type.like(sample_type_I),
                    data_stage01_isotopomer_normalized.scan_type.like(scan_type_I),
                    data_stage01_isotopomer_normalized.used_.is_(True)).group_by(
                    data_stage01_isotopomer_normalized.met_id).order_by(
                    data_stage01_isotopomer_normalized.met_id.asc()).all();
            met_ids_O = [];
            if not(met_ids):
                print("no results found")
                print("experiment_id_I	sample_name_abbreviation_I	time_point_I	scan_type_I");
                print(experiment_id_I,sample_name_abbreviation_I,time_point_I,scan_type_I);
            else:
                for cn in met_ids:
                    met_ids_O.append(cn[0]);
                return met_ids_O;
        except SQLAlchemyError as e:
            print(e);
    # Query met ids and other information from data_stage01_isotopomer_normalized
    def get_metIDsAndOther_experimentIDAndSampleAbbreviationAndTimePointAndDilutionAndScanTypeAndMetID_dataStage01Normalized(self,experiment_id_I,sample_name_abbreviation_I,time_point_I,dilution_I,scan_type_I,met_id_I):
        '''Querry met ids, fragment formulas, and fragment masses, that are used for the experiment, sample abbreviation, time point, dilution, scan type, and met_ID'''
        try:
            met_ids = self.session.query(data_stage01_isotopomer_normalized.met_id,
                    data_stage01_isotopomer_normalized.fragment_formula,
                    data_stage01_isotopomer_normalized.fragment_mass).filter(
                    data_stage01_isotopomer_normalized.sample_name_abbreviation.like(sample_name_abbreviation_I),
                    data_stage01_isotopomer_normalized.experiment_id.like(experiment_id_I),
                    data_stage01_isotopomer_normalized.time_point.like(time_point_I),
                    data_stage01_isotopomer_normalized.dilution == dilution_I,
                    data_stage01_isotopomer_normalized.scan_type.like(scan_type_I),
                    data_stage01_isotopomer_normalized.met_id.like(met_id_I),
                    data_stage01_isotopomer_normalized.used_.is_(True)).group_by(
                    data_stage01_isotopomer_normalized.met_id,
                    data_stage01_isotopomer_normalized.fragment_formula,
                    data_stage01_isotopomer_normalized.fragment_mass).order_by(
                    data_stage01_isotopomer_normalized.fragment_mass.asc(),
                    data_stage01_isotopomer_normalized.fragment_formula.desc(),
                    data_stage01_isotopomer_normalized.met_id.asc()).all();
            met_ids_O = [];
            fragment_formulas_O = [];
            fragment_masses_O = [];
            if not(met_ids):
                print("no results found")
                print("experiment_id_I	sample_name_abbreviation_I	time_point_I	dilution_I	scan_type_I	met_id_I");
                print(experiment_id_I,sample_name_abbreviation_I,time_point_I,dilution_I,scan_type_I,met_id_I);
            else:
                for cn in met_ids:
                    met_ids_O.append(cn.met_id);
                    fragment_formulas_O.append(cn.fragment_formula);
                    fragment_masses_O.append(cn.fragment_mass);
                return met_ids_O,fragment_formulas_O,fragment_masses_O;
        except SQLAlchemyError as e:
            print(e);
    def get_metIDsAndOther_experimentIDAndSampleAbbreviationAndTimePointAndDilutionAndScanType_dataStage01Normalized(self,experiment_id_I,sample_name_abbreviation_I,time_point_I,dilution_I,scan_type_I):
        '''Querry met ids, fragment formulas, and fragment masses, that are used for the experiment, sample abbreviation, time point, dilution, scan type'''
        try:
            met_ids = self.session.query(data_stage01_isotopomer_normalized.met_id,
                    data_stage01_isotopomer_normalized.fragment_formula,
                    data_stage01_isotopomer_normalized.fragment_mass).filter(
                    data_stage01_isotopomer_normalized.sample_name_abbreviation.like(sample_name_abbreviation_I),
                    data_stage01_isotopomer_normalized.experiment_id.like(experiment_id_I),
                    data_stage01_isotopomer_normalized.time_point.like(time_point_I),
                    data_stage01_isotopomer_normalized.dilution == dilution_I,
                    data_stage01_isotopomer_normalized.scan_type.like(scan_type_I),
                    data_stage01_isotopomer_normalized.used_.is_(True)).group_by(
                    data_stage01_isotopomer_normalized.met_id,
                    data_stage01_isotopomer_normalized.fragment_formula,
                    data_stage01_isotopomer_normalized.fragment_mass).order_by(
                    data_stage01_isotopomer_normalized.fragment_mass.asc(),
                    data_stage01_isotopomer_normalized.fragment_formula.desc(),
                    data_stage01_isotopomer_normalized.met_id.asc()).all();
            met_ids_O = [];
            fragment_formulas_O = [];
            fragment_masses_O = [];
            if not(met_ids):
                print("no results found")
                print("experiment_id_I	sample_name_abbreviation_I	time_point_I	dilution_I	scan_type_I	met_id_I");
                print(experiment_id_I,sample_name_abbreviation_I,time_point_I,dilution_I,scan_type_I,met_id_I);
            else:
                for cn in met_ids:
                    met_ids_O.append(cn.met_id);
                    fragment_formulas_O.append(cn.fragment_formula);
                    fragment_masses_O.append(cn.fragment_mass);
                return met_ids_O,fragment_formulas_O,fragment_masses_O;
        except SQLAlchemyError as e:
            print(e);
    # Query fragment formulas and masses from data_stage01_isotopomer_normalized
    def get_fragmentFormulasAndMass_experimentIDAndSampleAbbreviationAndTimePointAndScanTypeAndMetID_dataStage01Normalized(self,experiment_id_I,sample_name_abbreviation_I,time_point_I,scan_type_I,met_id_I):
        '''Querry fragment formulas and fragment masses, that are used for the experiment, sample abbreviation, time point, scan type, and met_ID'''
        try:
            met_ids = self.session.query(data_stage01_isotopomer_normalized.fragment_formula,
                    data_stage01_isotopomer_normalized.fragment_mass).filter(
                    data_stage01_isotopomer_normalized.sample_name_abbreviation.like(sample_name_abbreviation_I),
                    data_stage01_isotopomer_normalized.experiment_id.like(experiment_id_I),
                    data_stage01_isotopomer_normalized.time_point.like(time_point_I),
                    data_stage01_isotopomer_normalized.scan_type.like(scan_type_I),
                    data_stage01_isotopomer_normalized.met_id.like(met_id_I),
                    data_stage01_isotopomer_normalized.used_.is_(True)).group_by(
                    data_stage01_isotopomer_normalized.fragment_formula,
                    data_stage01_isotopomer_normalized.fragment_mass).order_by(
                    data_stage01_isotopomer_normalized.fragment_formula.desc(),
                    data_stage01_isotopomer_normalized.fragment_mass.asc()).all();
            fragment_formulas_O = [];
            fragment_masses_O = [];
            if not(met_ids):
                print("no results found")
                print("experiment_id_I	sample_name_abbreviation_I	time_point_I	scan_type_I	met_id_I");
                print(experiment_id_I,sample_name_abbreviation_I,time_point_I,scan_type_I,met_id_I);
            else:
                for cn in met_ids:
                    fragment_formulas_O.append(cn.fragment_formula);
                    fragment_masses_O.append(cn.fragment_mass);
                return fragment_formulas_O,fragment_masses_O;
        except SQLAlchemyError as e:
            print(e);
    def get_fragmentFormulasAndMass_experimentIDAndSampleAbbreviationAndTimePointAndAndSampleTypeAndScanTypeAndMetID_dataStage01Normalized(self,experiment_id_I,sample_name_abbreviation_I,time_point_I,sample_type_I,scan_type_I,met_id_I):
        '''Querry fragment formulas and fragment masses, that are used for the experiment, sample abbreviation, time point, scan type, and met_ID'''
        try:
            met_ids = self.session.query(data_stage01_isotopomer_normalized.fragment_formula,
                    data_stage01_isotopomer_normalized.fragment_mass).filter(
                    data_stage01_isotopomer_normalized.sample_name_abbreviation.like(sample_name_abbreviation_I),
                    data_stage01_isotopomer_normalized.experiment_id.like(experiment_id_I),
                    data_stage01_isotopomer_normalized.sample_type.like(sample_type_I),
                    data_stage01_isotopomer_normalized.time_point.like(time_point_I),
                    data_stage01_isotopomer_normalized.scan_type.like(scan_type_I),
                    data_stage01_isotopomer_normalized.met_id.like(met_id_I),
                    data_stage01_isotopomer_normalized.used_.is_(True)).group_by(
                    data_stage01_isotopomer_normalized.fragment_formula,
                    data_stage01_isotopomer_normalized.fragment_mass).order_by(
                    data_stage01_isotopomer_normalized.fragment_formula.desc(),
                    data_stage01_isotopomer_normalized.fragment_mass.asc()).all();
            fragment_formulas_O = [];
            fragment_masses_O = [];
            if not(met_ids):
                print("no results found")
                print("experiment_id_I	sample_name_abbreviation_I	time_point_I	scan_type_I	met_id_I");
                print(experiment_id_I,sample_name_abbreviation_I,time_point_I,scan_type_I,met_id_I);
            else:
                for cn in met_ids:
                    fragment_formulas_O.append(cn.fragment_formula);
                    fragment_masses_O.append(cn.fragment_mass);
                return fragment_formulas_O,fragment_masses_O;
        except SQLAlchemyError as e:
            print(e);
    # query sample dilutions from data_stage01_normalized
    def get_sampleDilution_experimentIDAndTimePoint_dataStage01Normalized(self,experiment_id_I,time_point_I):
        '''Querry dilutions that are used from the experiment'''
        try:
            sample_dilutions = self.session.query(data_stage01_isotopomer_normalized.dilution).filter(
                    data_stage01_isotopomer_normalized.experiment_id.like(experiment_id_I),
                    data_stage01_isotopomer_normalized.used_.is_(True),
                    data_stage01_isotopomer_normalized.time_point.like(time_point_I)).group_by(
                    data_stage01_isotopomer_normalized.dilution).order_by(
                    data_stage01_isotopomer_normalized.dilution.asc()).all();
            sample_dilutions_O = [];
            for sd in sample_dilutions: sample_dilutions_O.append(sd.dilution);
            return sample_dilutions_O;
        except SQLAlchemyError as e:
            print(e);
    # query time points from data_stage01_normalized
    def get_timePoint_experimentIDAndSampleNameAbbreviation_dataStage01Normalized(self,experiment_id_I,sample_name_abbreviation_I):
        '''Querry time points that are used from the experiment and sample name abbreviation'''
        try:
            time_points = self.session.query(sample_description.time_point).filter(
                    sample_description.sample_name_abbreviation.like(sample_name_abbreviation_I),
                    data_stage01_isotopomer_normalized.experiment_id.like(experiment_id_I),
                    data_stage01_isotopomer_normalized.used_.is_(True),
                    data_stage01_isotopomer_normalized.sample_name.like(sample.sample_name),
                    sample.sample_id.like(sample_description.sample_id)).group_by(
                    sample_description.time_point).order_by(
                    sample_description.time_point.asc()).all();
            time_points_O = [];
            for tp in time_points: time_points_O.append(tp.time_point);
            return time_points_O;
        except SQLAlchemyError as e:
            print(e);
    def get_timePoint_experimentID_dataStage01Normalized(self,experiment_id_I):
        '''Querry time points that are used from the experiment and sample name'''
        try:
            time_points = self.session.query(data_stage01_isotopomer_normalized.time_point).filter(
                    data_stage01_isotopomer_normalized.experiment_id.like(experiment_id_I),
                    data_stage01_isotopomer_normalized.used_.is_(True)).group_by(
                    data_stage01_isotopomer_normalized.time_point).order_by(
                    data_stage01_isotopomer_normalized.time_point.asc()).all();
            time_points_O = [];
            for tp in time_points: 
                if tp.time_point: time_points_O.append(tp.time_point);
            return time_points_O;
        except SQLAlchemyError as e:
            print(e);
    def get_timePoint_experimentIDAndComment_dataStage01Normalized(self,experiment_id_I,comment_I):
        '''Querry time points that are used from the experiment and sample name'''
        try:
            time_points = self.session.query(data_stage01_isotopomer_normalized.time_point).filter(
                    data_stage01_isotopomer_normalized.experiment_id.like(experiment_id_I),
                    data_stage01_isotopomer_normalized.comment_.like(comment_I),
                    data_stage01_isotopomer_normalized.used_.is_(True)).group_by(
                    data_stage01_isotopomer_normalized.time_point).order_by(
                    data_stage01_isotopomer_normalized.time_point.asc()).all();
            time_points_O = [];
            for tp in time_points: time_points_O.append(tp.time_point);
            return time_points_O;
        except SQLAlchemyError as e:
            print(e);
    # query replicate numbers from data_stage01_isotopomer_normalized
    def get_replicateNumbers_experimentIDAndSampleAbbreviationAndTimePointAndScanTypeAndMetID_dataStage01Normalized(self,experiment_id_I,sample_name_abbreviation_I,time_point_I,scan_type_I,met_id_I):
        '''Querry replicate numbers that are used for the experiment, sample abbreviation, time point, scan type, and met_id'''
        try:
            replicate_numbers = self.session.query(data_stage01_isotopomer_normalized.replicate_number).filter(
                    data_stage01_isotopomer_normalized.sample_name_abbreviation.like(sample_name_abbreviation_I),
                    data_stage01_isotopomer_normalized.met_id.like(met_id_I),
                    data_stage01_isotopomer_normalized.experiment_id.like(experiment_id_I),
                    data_stage01_isotopomer_normalized.time_point.like(time_point_I),
                    data_stage01_isotopomer_normalized.scan_type.like(scan_type_I),
                    data_stage01_isotopomer_normalized.used_.is_(True)).group_by(
                    data_stage01_isotopomer_normalized.replicate_number).order_by(
                    data_stage01_isotopomer_normalized.replicate_number.asc()).all();
            replicate_numbers_O = [];
            if not(replicate_numbers):
                print("no results found")
                print("experiment_id_I	sample_name_abbreviation_I	time_point_I	scan_type_I met_id_I");
                print(experiment_id_I,sample_name_abbreviation_I,time_point_I,scan_type_I,met_id_I);
            else:
                for cn in replicate_numbers:
                    replicate_numbers_O.append(cn.replicate_number);
                return replicate_numbers_O;
        except SQLAlchemyError as e:
            print(e);
    # query normalized intensity from data_stage01_isotopomer_normalized
    def get_normalizedIntensity_experimentIDAndSampleAbbreviationAndTimePointAndReplicateNumberAndMetIDAndFragmentFormulaAndMassAndScanType_dataStage01Normalized(self,experiment_id_I,sample_name_abbreviation_I,time_point_I,replicate_number_I,met_id_I,fragment_formula_I,fragment_mass_I,scan_type_I):
        '''Querry peak data for a specific experiment_id, sample_name, met_id, and scan type'''
        try:
            data = self.session.query(data_stage01_isotopomer_normalized.intensity_normalized,
                    data_stage01_isotopomer_normalized.intensity_normalized_units).filter(
                    data_stage01_isotopomer_normalized.sample_name_abbreviation.like(sample_name_abbreviation_I),
                    data_stage01_isotopomer_normalized.time_point.like(time_point_I),
                    data_stage01_isotopomer_normalized.fragment_formula.like(fragment_formula_I),
                    data_stage01_isotopomer_normalized.fragment_mass == fragment_mass_I,
                    data_stage01_isotopomer_normalized.experiment_id.like(experiment_id_I),
                    data_stage01_isotopomer_normalized.met_id.like(met_id_I),
                    data_stage01_isotopomer_normalized.scan_type.like(scan_type_I),
                    data_stage01_isotopomer_normalized.replicate_number == replicate_number_I,
                    data_stage01_isotopomer_normalized.used_).all();
            intensity_normalized_O = None;
            intensity_normalized_units_O = None;
            if not data:
                print('No normalized intensities found for the following:')
                print('sample_name_abbreviation\ttime_point\treplicate_number\tmet_id\tfragment_formula\tfragment_mass\tscan_type');
                print((sample_name_abbreviation_I) + '\t' + str(time_point_I) + '\t' + str(replicate_number_I) + '\t' + str(met_id_I) + '\t' + str(fragment_formula_I) + '\t' + str(fragment_mass_I) + '\t' + str(scan_type_I));
                return intensity_normalized_O;
            else:
                intensity_normalized_O = data[0][0];
                intensity_normalized_units_O = data[0][1];
                return intensity_normalized_O;
        except SQLAlchemyError as e:
            print(e);
    def get_normalizedIntensity_experimentIDAndSampleAbbreviationAndTimePointAndMetIDAndFragmentFormulaAndMassAndScanType_dataStage01Normalized(self,experiment_id_I,sample_name_abbreviation_I,time_point_I,met_id_I,fragment_formula_I,fragment_mass_I,scan_type_I):
        '''Querry peak data for a specific experiment_id, sample_name, met_id, and scan type'''
        try:
            data = self.session.query(data_stage01_isotopomer_normalized.intensity_normalized,
                    data_stage01_isotopomer_normalized.intensity_normalized_units).filter(
                    data_stage01_isotopomer_normalized.sample_name_abbreviation.like(sample_name_abbreviation_I),
                    data_stage01_isotopomer_normalized.time_point.like(time_point_I),
                    data_stage01_isotopomer_normalized.fragment_formula.like(fragment_formula_I),
                    data_stage01_isotopomer_normalized.fragment_mass == fragment_mass_I,
                    data_stage01_isotopomer_normalized.experiment_id.like(experiment_id_I),
                    data_stage01_isotopomer_normalized.met_id.like(met_id_I),
                    data_stage01_isotopomer_normalized.scan_type.like(scan_type_I),
                    data_stage01_isotopomer_normalized.used_).all();
            intensity_normalized_O = [];
            intensity_normalized_units_O = [];
            if not data:
                print('No normalized intensities found for the following:')
                print('sample_name_abbreviation\ttime_point\tmet_id\tfragment_formula\tfragment_mass\tscan_type');
                print((sample_name_abbreviation_I) + '\t' + str(time_point_I) + '\t' + str(met_id_I) + '\t' + str(fragment_formula_I) + '\t' + str(fragment_mass_I) + '\t' + str(scan_type_I));
                return intensity_normalized_O;
            else:
                for d in data:
                    if d.intensity_normalized and not d.intensity_normalized == 0.0: # skip replicates without a value or 0.0
                        intensity_normalized_O.append(d.intensity_normalized);
                        intensity_normalized_units_O.append(d.intensity_normalized_units);
                if intensity_normalized_O: return intensity_normalized_O;
                else: return [0.0];
        except SQLAlchemyError as e:
            print(e);
    def get_normalizedIntensity_experimentIDAndSampleAbbreviationAndTimePointAndSampleTypeAndMetIDAndFragmentFormulaAndMassAndScanType_dataStage01Normalized(self,experiment_id_I,sample_name_abbreviation_I,time_point_I,sample_type_I,met_id_I,fragment_formula_I,fragment_mass_I,scan_type_I):
        '''Querry peak data for a specific experiment_id, sample_name, met_id, and scan type'''
        try:
            data = self.session.query(data_stage01_isotopomer_normalized.intensity_normalized,
                    data_stage01_isotopomer_normalized.intensity_normalized_units).filter(
                    data_stage01_isotopomer_normalized.sample_name_abbreviation.like(sample_name_abbreviation_I),
                    data_stage01_isotopomer_normalized.sample_type.like(sample_type_I),
                    data_stage01_isotopomer_normalized.time_point.like(time_point_I),
                    data_stage01_isotopomer_normalized.fragment_formula.like(fragment_formula_I),
                    data_stage01_isotopomer_normalized.fragment_mass == fragment_mass_I,
                    data_stage01_isotopomer_normalized.experiment_id.like(experiment_id_I),
                    data_stage01_isotopomer_normalized.met_id.like(met_id_I),
                    data_stage01_isotopomer_normalized.scan_type.like(scan_type_I),
                    data_stage01_isotopomer_normalized.used_).all();
            intensity_normalized_O = [];
            intensity_normalized_units_O = [];
            if not data:
                print('No normalized intensities found for the following:')
                print('sample_name_abbreviation\ttime_point\tmet_id\tfragment_formula\tfragment_mass\tscan_type');
                print((sample_name_abbreviation_I) + '\t' + str(time_point_I) + '\t' + str(met_id_I) + '\t' + str(fragment_formula_I) + '\t' + str(fragment_mass_I) + '\t' + str(scan_type_I));
                return intensity_normalized_O;
            else:
                for d in data:
                    if d.intensity_normalized and not d.intensity_normalized == 0.0: # skip replicates without a value or 0.0
                        intensity_normalized_O.append(d.intensity_normalized);
                        intensity_normalized_units_O.append(d.intensity_normalized_units);
                if intensity_normalized_O: return intensity_normalized_O;
                else: return [0.0];
        except SQLAlchemyError as e:
            print(e);
    # query data from data_stage01_isotopomer_normalized
    def get_data_experimentIDAndSampleNameAndMetIDAndAndScanType_normalized(self,experiment_id_I,sample_name_I,met_id_I,scan_type_I):
        '''Querry peak data for a specific experiment_id, sample_name, met_id, and scan type'''
        try:
            data = self.session.query(data_stage01_isotopomer_normalized.fragment_formula,
                    data_stage01_isotopomer_normalized.fragment_mass,
                    data_stage01_isotopomer_normalized.intensity_corrected,
                    data_stage01_isotopomer_normalized.intensity_corrected_units).filter(
                    data_stage01_isotopomer_normalized.sample_name.like(sample_name_I),
                    data_stage01_isotopomer_normalized.experiment_id.like(experiment_id_I),
                    data_stage01_isotopomer_normalized.met_id.like(met_id_I),
                    data_stage01_isotopomer_normalized.scan_type.like(scan_type_I),
                    data_stage01_isotopomer_normalized.used_).order_by(
                    data_stage01_isotopomer_normalized.fragment_formula.asc(),
                    data_stage01_isotopomer_normalized.fragment_mass.asc()).all();
            fragment_formula = '';
            fragment_formula_old = '';
            data_O = {};
            if not data:
                print(('No data found for sample_name: ' + sample_name_I + ', met_id: ' + met_id_I));
                return data_O;
            else:
                mass_O = {};
                for i,d in enumerate(data):
                    if i==0:
                        fragment_formula_old = d.fragment_formula;
                        mass_O[d.fragment_mass] = d.intensity_corrected;
                    fragment_formula = d.fragment_formula;
                    if fragment_formula != fragment_formula_old:
                        data_O[fragment_formula_old] = mass_O;
                        fragment_formula_old = fragment_formula
                        mass_O = {};
                    elif i == len(data)-1 and fragment_formula == fragment_formula_old:
                        mass_O[d.fragment_mass] = d.intensity_corrected;
                        data_O[fragment_formula] = mass_O;
                    mass_O[d.fragment_mass] = d.intensity_corrected;
                return data_O;
        except SQLAlchemyError as e:
            print(e);
    def get_data_experimentIDAndSampleAbbreviationAndTimePointAndScanTypeAndMetIDAndReplicateNumber_dataStage01Normalized(self,experiment_id_I,sample_name_abbreviation_I,time_point_I,scan_type_I,met_id_I,replicate_number_I):
        '''Querry peak data that are used for the experiment, sample abbreviation, time point, scan type, met_id, and replicate number'''
        try:
            data = self.session.query(data_stage01_isotopomer_normalized.dilution,
                    data_stage01_isotopomer_normalized.fragment_formula,
                    data_stage01_isotopomer_normalized.fragment_mass,
                    data_stage01_isotopomer_normalized.intensity_normalized,
                    data_stage01_isotopomer_normalized.intensity_normalized_units,
                    data_stage01_isotopomer_normalized.used_,
                    data_stage01_isotopomer_normalized.comment_).filter(
                    data_stage01_isotopomer_normalized.sample_name_abbreviation.like(sample_name_abbreviation_I),
                    data_stage01_isotopomer_normalized.met_id.like(met_id_I),
                    data_stage01_isotopomer_normalized.experiment_id.like(experiment_id_I),
                    data_stage01_isotopomer_normalized.time_point.like(time_point_I),
                    data_stage01_isotopomer_normalized.scan_type.like(scan_type_I),
                    data_stage01_isotopomer_normalized.replicate_number == replicate_number_I,
                    data_stage01_isotopomer_normalized.used_.is_(True)).order_by(
                    data_stage01_isotopomer_normalized.fragment_formula.asc(),
                    data_stage01_isotopomer_normalized.fragment_mass.asc(),
                    data_stage01_isotopomer_normalized.dilution.asc()).all();
            fragment_formula = '';
            fragment_formula_old = '';
            data_O = {};
            if not data:
                print('No data found');
                return data_O;
            else:
                ## extract out dilutions
                #dilutions = [d.dilution for d in data];
                #dilutions = list(set(dilutions));
                #dilutions.sort();
                #dilutions_dict = dict(zip(dilutions,['low','high']));
                mass_lst = [];
                mass_O = {};
                for i,d in enumerate(data):
                    info = {};
                    if i==0:
                        fragment_formula_old = d.fragment_formula;
                    fragment_formula = d.fragment_formula;
                    if fragment_formula != fragment_formula_old:
                        data_O[fragment_formula_old] = mass_lst;
                        fragment_formula_old = fragment_formula
                        mass_lst = [];
                        info['intensity'] = d.intensity_normalized;
                        info['dilution'] = d.dilution;
                        info['used_'] = d.used_;
                        info['comment_'] = d.comment_;
                        mass_O[d.fragment_mass] = info;
                        mass_lst.append(mass_O);
                        mass_O = {};
                    elif i == len(data)-1 and fragment_formula == fragment_formula_old:
                        info['intensity'] = d.intensity_normalized;
                        info['dilution'] = d.dilution;
                        info['used_'] = d.used_;
                        info['comment_'] = d.comment_;
                        mass_O[d.fragment_mass] = info;
                        mass_lst.append(mass_O);
                        mass_O = {};               
                        data_O[fragment_formula] = mass_lst;
                    else:
                        info['intensity'] = d.intensity_normalized;
                        info['dilution'] = d.dilution;
                        info['used_'] = d.used_;
                        info['comment_'] = d.comment_;
                        mass_O[d.fragment_mass] = info;
                        mass_lst.append(mass_O);
                        mass_O = {};
                return data_O;
        except SQLAlchemyError as e:
            print(e);
    def get_dataNormalized_experimentIDAndSampleAbbreviationAndTimePointAndScanTypeAndMetIDAndReplicateNumber_dataStage01Normalized(self,experiment_id_I,sample_name_abbreviation_I,time_point_I,scan_type_I,met_id_I,replicate_number_I):
        '''Querry peak data that are used for the experiment, sample abbreviation, time point, scan type, met_id, and replicate number'''
        try:
            data = self.session.query(data_stage01_isotopomer_normalized.dilution,
                    data_stage01_isotopomer_normalized.fragment_formula,
                    data_stage01_isotopomer_normalized.fragment_mass,
                    data_stage01_isotopomer_normalized.intensity_normalized,
                    data_stage01_isotopomer_normalized.intensity_normalized_units,
                    data_stage01_isotopomer_normalized.used_,
                    data_stage01_isotopomer_normalized.comment_).filter(
                    data_stage01_isotopomer_normalized.sample_name_abbreviation.like(sample_name_abbreviation_I),
                    data_stage01_isotopomer_normalized.met_id.like(met_id_I),
                    data_stage01_isotopomer_normalized.experiment_id.like(experiment_id_I),
                    data_stage01_isotopomer_normalized.time_point.like(time_point_I),
                    data_stage01_isotopomer_normalized.scan_type.like(scan_type_I),
                    data_stage01_isotopomer_normalized.replicate_number == replicate_number_I,
                    data_stage01_isotopomer_normalized.used_.is_(True)).order_by(
                    data_stage01_isotopomer_normalized.fragment_formula.asc(),
                    data_stage01_isotopomer_normalized.fragment_mass.asc(),
                    data_stage01_isotopomer_normalized.dilution.asc()).all();
            fragment_formula = '';
            fragment_formula_old = '';
            data_O = {};
            if not data:
                print('No data found');
                return data_O;
            else:
                mass_O = {};
                for i,d in enumerate(data):
                    if i==0:
                        fragment_formula_old = d.fragment_formula;
                        mass_O[d.fragment_mass] = d.intensity_normalized;
                    fragment_formula = d.fragment_formula;
                    if fragment_formula != fragment_formula_old:
                        data_O[fragment_formula_old] = mass_O;
                        fragment_formula_old = fragment_formula
                        mass_O = {};
                    elif i == len(data)-1 and fragment_formula == fragment_formula_old:
                        mass_O[d.fragment_mass] = d.intensity_normalized;
                        data_O[fragment_formula] = mass_O;
                    mass_O[d.fragment_mass] = d.intensity_normalized;
                return data_O;
        except SQLAlchemyError as e:
            print(e);
    def get_dataNormalized_experimentIDAndSampleAbbreviationAndTimePointAndScanTypeAndMetIDAndSampleName_dataStage01Normalized(self,experiment_id_I,sample_name_abbreviation_I,time_point_I,scan_type_I,met_id_I,sample_name_I):
        '''Querry peak data that are used for the experiment, sample abbreviation, time point, scan type, met_id, and sample_name'''
        try:
            data = self.session.query(data_stage01_isotopomer_normalized.dilution,
                    data_stage01_isotopomer_normalized.fragment_formula,
                    data_stage01_isotopomer_normalized.fragment_mass,
                    data_stage01_isotopomer_normalized.intensity_normalized,
                    data_stage01_isotopomer_normalized.intensity_normalized_units,
                    data_stage01_isotopomer_normalized.used_,
                    data_stage01_isotopomer_normalized.comment_).filter(
                    data_stage01_isotopomer_normalized.sample_name_abbreviation.like(sample_name_abbreviation_I),
                    data_stage01_isotopomer_normalized.met_id.like(met_id_I),
                    data_stage01_isotopomer_normalized.experiment_id.like(experiment_id_I),
                    data_stage01_isotopomer_normalized.time_point.like(time_point_I),
                    data_stage01_isotopomer_normalized.scan_type.like(scan_type_I),
                    data_stage01_isotopomer_normalized.sample_name.like(sample_name_I),
                    data_stage01_isotopomer_normalized.used_.is_(True)).order_by(
                    data_stage01_isotopomer_normalized.fragment_formula.asc(),
                    data_stage01_isotopomer_normalized.fragment_mass.asc(),
                    data_stage01_isotopomer_normalized.dilution.asc()).all();
            fragment_formula = '';
            fragment_formula_old = '';
            data_O = {};
            if not data:
                print('No data found');
                return data_O;
            else:
                mass_O = {};
                for i,d in enumerate(data):
                    if i==0:
                        fragment_formula_old = d.fragment_formula;
                        mass_O[d.fragment_mass] = d.intensity_normalized;
                    fragment_formula = d.fragment_formula;
                    if fragment_formula != fragment_formula_old:
                        data_O[fragment_formula_old] = mass_O;
                        fragment_formula_old = fragment_formula
                        mass_O = {};
                    elif i == len(data)-1 and fragment_formula == fragment_formula_old:
                        mass_O[d.fragment_mass] = d.intensity_normalized;
                        data_O[fragment_formula] = mass_O;
                    mass_O[d.fragment_mass] = d.intensity_normalized;
                return data_O;
        except SQLAlchemyError as e:
            print(e);
    def get_rows_experimentID_dataStage01Normalized(self,experiment_id_I):
        '''Query rows for a specific experiment_id'''
        try:
            data = self.session.query(data_stage01_isotopomer_normalized).filter(
                    data_stage01_isotopomer_normalized.experiment_id.like(experiment_id_I),
                    data_stage01_isotopomer_normalized.used_).order_by(
                    data_stage01_isotopomer_normalized.fragment_formula.asc(),
                    data_stage01_isotopomer_normalized.fragment_mass.asc(),
                    data_stage01_isotopomer_normalized.sample_name.asc()).all();
            data_O = [];
            if not data:
                return data_O;
            else:
                for d in data:
                    data_O.append(d.__repr__dict__());
                return data_O;
        except SQLAlchemyError as e:
            print(e);
    def get_rows_experimentIDAndSampleAbbreviationAndTimePointAndDilutionAndScanTypeAndMetID_dataStage01Normalized(self,experiment_id_I,sample_name_abbreviation_I,time_point_I,dilution_I,scan_type_I,met_id_I):
        '''Querry rows that are used for the experiment, sample abbreviation, time point, dilution, scan type, and met_ids'''
        try:
            data = self.session.query(data_stage01_isotopomer_normalized).filter(
                    data_stage01_isotopomer_normalized.sample_name_abbreviation.like(sample_name_abbreviation_I),
                    data_stage01_isotopomer_normalized.experiment_id.like(experiment_id_I),
                    data_stage01_isotopomer_normalized.time_point.like(time_point_I),
                    data_stage01_isotopomer_normalized.dilution == dilution_I,
                    data_stage01_isotopomer_normalized.scan_type.like(scan_type_I),
                    data_stage01_isotopomer_normalized.met_id.like(met_id_I),
                    data_stage01_isotopomer_normalized.used_.is_(True)).order_by(
                    data_stage01_isotopomer_normalized.fragment_formula.asc(),
                    data_stage01_isotopomer_normalized.fragment_mass.asc(),
                    data_stage01_isotopomer_normalized.sample_name.asc()).all();
            data_O = [];
            if not data:
                return data_O;
            else:
                for d in data:
                    data_O.append(d.__repr__dict__());
                return data_O;
        except SQLAlchemyError as e:
            print(e);
    def get_rows_experimentIDAndSampleAbbreviationAndTimePointAndScanTypeAndMetID_dataStage01Normalized(self,experiment_id_I,sample_name_abbreviation_I,time_point_I,scan_type_I,met_id_I):
        '''Querry rows that are used for the experiment, sample abbreviation, time point, dilution, scan type, and met_ids'''
        try:
            data = self.session.query(data_stage01_isotopomer_normalized).filter(
                    data_stage01_isotopomer_normalized.sample_name_abbreviation.like(sample_name_abbreviation_I),
                    data_stage01_isotopomer_normalized.experiment_id.like(experiment_id_I),
                    data_stage01_isotopomer_normalized.time_point.like(time_point_I),
                    data_stage01_isotopomer_normalized.scan_type.like(scan_type_I),
                    data_stage01_isotopomer_normalized.met_id.like(met_id_I),
                    data_stage01_isotopomer_normalized.used_.is_(True)).order_by(
                    data_stage01_isotopomer_normalized.fragment_formula.asc(),
                    data_stage01_isotopomer_normalized.fragment_mass.asc(),
                    data_stage01_isotopomer_normalized.sample_name.asc()).all();
            data_O = [];
            if not data:
                return data_O;
            else:
                for d in data:
                    data_O.append(d.__repr__dict__());
                return data_O;
        except SQLAlchemyError as e:
            print(e);
    # update data for data_stage01_isotopomer_normalized
    def update_data_stage01_isotopomer_normalized(self,dataListUpdated_I):
        # update the data_stage01_isotopomer_normalized
        updates = [];
        for d in dataListUpdated_I:
            if 'intensity_corrected' in d:
                try:
                    data_update = self.session.query(data_stage01_isotopomer_normalized).filter(
                            data_stage01_isotopomer_normalized.experiment_id.like(d['experiment_id']),
                            data_stage01_isotopomer_normalized.sample_name_abbreviation.like(d['sample_name_abbreviation']),
                            data_stage01_isotopomer_normalized.time_point.like(d['time_point']),
                            data_stage01_isotopomer_normalized.dilution == d['dilution'],
                            data_stage01_isotopomer_normalized.sample_type.like(d['sample_type']),
                            data_stage01_isotopomer_normalized.replicate_number == d['replicate_number'],
                            data_stage01_isotopomer_normalized.met_id.like(d['met_id']),
                            data_stage01_isotopomer_normalized.fragment_formula.like(d['fragment_formula']),
                            data_stage01_isotopomer_normalized.fragment_mass == d['fragment_mass'],
                            data_stage01_isotopomer_normalized.scan_type.like(d['scan_type'])).update(		
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
                        #row = data_stage01_isotopomer_normalized();
                        #self.session.add(row);
                        #self.session.commit();
                    #elif data_update ==1:
                    #    print 'good update'
                    updates.append(data_update);
                except SQLAlchemyError as e:
                    print(e);
            elif 'used_' in d:
                try:
                    data_update = self.session.query(data_stage01_isotopomer_normalized).filter(
                            data_stage01_isotopomer_normalized.experiment_id.like(d['experiment_id']),
                            data_stage01_isotopomer_normalized.sample_name_abbreviation.like(d['sample_name_abbreviation']),
                            data_stage01_isotopomer_normalized.time_point.like(d['time_point']),
                            data_stage01_isotopomer_normalized.dilution == d['dilution'],
                            data_stage01_isotopomer_normalized.replicate_number == d['replicate_number'],
                            data_stage01_isotopomer_normalized.met_id.like(d['met_id']),
                            data_stage01_isotopomer_normalized.fragment_formula.like(d['fragment_formula']),
                            data_stage01_isotopomer_normalized.fragment_mass == d['fragment_mass'],
                            data_stage01_isotopomer_normalized.scan_type.like(d['scan_type'])).update(		
                            {
                            # 'intensity':d['intensity'],
                            #'intensity_units':d['intensity_units'],
                            'intensity_normalized':d['intensity_normalized'],
                            'intensity_normalized_units':d['intensity_normalized_units'],
                            'abs_devFromTheoretical':d['abs_devFromTheoretical'],
                            'used_':d['used_'],
                            'comment_':d['comment_']},
                            synchronize_session=False);
                    if data_update == 0:
                        print('row not found.')
                        print(d)
                    #elif data_update ==1:
                    #    print 'good update'
                    updates.append(data_update);
                except SQLAlchemyError as e:
                    print(e);
        self.session.commit();
    def update_dataStage01IsotopomerNormalized_byUniqueConstraint(self,dataListUpdated_I):
        # update the data_stage01_isotopomer_normalized
        updates = [];
        for d in dataListUpdated_I:
            try:
                data_update = self.session.query(data_stage01_isotopomer_normalized).filter(
                        data_stage01_isotopomer_normalized.experiment_id.like(d['experiment_id']),
                        data_stage01_isotopomer_normalized.sample_name_abbreviation.like(d['sample_name_abbreviation']),
                        data_stage01_isotopomer_normalized.time_point.like(d['time_point']),
                        data_stage01_isotopomer_normalized.dilution == d['dilution'],
                        data_stage01_isotopomer_normalized.sample_type.like(d['sample_type']),
                        data_stage01_isotopomer_normalized.replicate_number == d['replicate_number'],
                        data_stage01_isotopomer_normalized.met_id.like(d['met_id']),
                        data_stage01_isotopomer_normalized.fragment_formula.like(d['fragment_formula']),
                        data_stage01_isotopomer_normalized.fragment_mass == d['fragment_mass'],
                        data_stage01_isotopomer_normalized.scan_type.like(d['scan_type'])).update(		
                        {
                            
                        'intensity_theoretical':d['intensity_theoretical'],
                        'abs_devFromTheoretical':d['abs_devFromTheoretical'],
                            
                        'intensity':d['intensity'],
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
                    #print 'row will be added.'
                    #row = data_stage01_isotopomer_normalized();
                    #self.session.add(row);
                    #self.session.commit();
                #elif data_update ==1:
                #    print 'good update'
                updates.append(data_update);
            except SQLAlchemyError as e:
                print(e);
        self.session.commit();
    def update_usedAndComment_stage01_isotopomer_normalized(self,dataListUpdated_I):
        # update the data_stage01_isotopomer_normalized used and comment columns from data_stage01_isotopomer_averages
        updates = [];
        for d in dataListUpdated_I:
            if d['used_'] and d['comment_']:
                #update only the comments
                try:
                    data_update = self.session.query(data_stage01_isotopomer_normalized).filter(
                            data_stage01_isotopomer_normalized.experiment_id.like(d['experiment_id']),
                            data_stage01_isotopomer_normalized.sample_name_abbreviation.like(d['sample_name_abbreviation']),
                            data_stage01_isotopomer_normalized.time_point.like(d['time_point']),
                            data_stage01_isotopomer_normalized.sample_type.like(d['sample_type']),
                            data_stage01_isotopomer_normalized.met_id.like(d['met_id']),
                            data_stage01_isotopomer_normalized.fragment_formula.like(d['fragment_formula']),
                            data_stage01_isotopomer_normalized.fragment_mass == d['fragment_mass'],
                            data_stage01_isotopomer_normalized.scan_type.like(d['scan_type'])).update(		
                            {
                            'comment_':d['comment_']},
                            synchronize_session=False);
                    if data_update == 0:
                        print('row not found.')
                        print(d)
                        #print 'row will be added.'
                        #row = data_stage01_isotopomer_normalized();
                        #self.session.add(row);
                        #self.session.commit();
                    #elif data_update ==1:
                    #    print 'good update'
                    updates.append(data_update);
                except SQLAlchemyError as e:
                    print(e);
            if not d['used_']:
                # update both used_ and comment_
                try:
                    data_update = self.session.query(data_stage01_isotopomer_normalized).filter(
                            data_stage01_isotopomer_normalized.experiment_id.like(d['experiment_id']),
                            data_stage01_isotopomer_normalized.sample_name_abbreviation.like(d['sample_name_abbreviation']),
                            data_stage01_isotopomer_normalized.time_point.like(d['time_point']),
                            data_stage01_isotopomer_normalized.sample_type.like(d['sample_type']),
                            data_stage01_isotopomer_normalized.met_id.like(d['met_id']),
                            data_stage01_isotopomer_normalized.fragment_formula.like(d['fragment_formula']),
                            data_stage01_isotopomer_normalized.fragment_mass == d['fragment_mass'],
                            data_stage01_isotopomer_normalized.scan_type.like(d['scan_type'])).update(		
                            {
                            'used_':d['used_'],
                            'comment_':d['comment_']},
                            synchronize_session=False);
                    if data_update == 0:
                        print('row not found.')
                        print(d)
                        #print 'row will be added.'
                        #row = data_stage01_isotopomer_normalized();
                        #self.session.add(row);
                        #self.session.commit();
                    #elif data_update ==1:
                    #    print 'good update'
                    updates.append(data_update);
                except SQLAlchemyError as e:
                    print(e);
        self.session.commit();

    def update_dataStage01IsotopomerNormalized(self,dataListUpdated_I):
        # update the data_stage01_isotopomer_normalized
        for d in dataListUpdated_I:
            try:
                data_update = self.session.query(data_stage01_isotopomer_normalized).filter(
                        data_stage01_isotopomer_normalized.id == d['id']).update(
                        #data_stage01_isotopomer_normalized.experiment_id.like(d['experiment_id']),
                        #data_stage01_isotopomer_normalized.sample_name_abbreviation.like(d['sample_name_abbreviation']),
                        #data_stage01_isotopomer_normalized.time_point.like(d['time_point']),
                        #data_stage01_isotopomer_normalized.dilution == d['dilution'],
                        #data_stage01_isotopomer_normalized.sample_type.like(d['sample_type']),
                        #data_stage01_isotopomer_normalized.replicate_number == d['replicate_number'],
                        #data_stage01_isotopomer_normalized.met_id.like(d['met_id']),
                        #data_stage01_isotopomer_normalized.fragment_formula.like(d['fragment_formula']),
                        #data_stage01_isotopomer_normalized.fragment_mass == d['fragment_mass']).update(		
                        {
                        'experiment_id':d['experiment_id'],
                        'sample_name_abbreviation':d['sample_name_abbreviation'],
                        'time_point':d['time_point'],
                        'dilution':d['dilution'],
                        'sample_type':d['sample_type'],
                        'replicate_number':d['replicate_number'],
                        'met_id':d['met_id'],
                        'fragment_formula':d['fragment_formula'],
                        'fragment_mass':d['fragment_mass'],
                        'intensity':d['intensity'],
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

    def updateUsedAndComment_dataStage01IsotopomerNormalized(self,dataListUpdated_I):
        # update the data_stage01_isotopomer_normalized
        for d in dataListUpdated_I:
            try:
                data_update = self.session.query(data_stage01_isotopomer_normalized).filter(
                        data_stage01_isotopomer_normalized.experiment_id.like(d['experiment_id']),
                        data_stage01_isotopomer_normalized.sample_name_abbreviation.like(d['sample_name_abbreviation']),
                        data_stage01_isotopomer_normalized.time_point.like(d['time_point']),
                        data_stage01_isotopomer_normalized.dilution == d['dilution'],
                        data_stage01_isotopomer_normalized.sample_type.like(d['sample_type']),
                        data_stage01_isotopomer_normalized.replicate_number == d['replicate_number'],
                        data_stage01_isotopomer_normalized.met_id.like(d['met_id']),
                        data_stage01_isotopomer_normalized.fragment_formula.like(d['fragment_formula']),
                        data_stage01_isotopomer_normalized.fragment_mass == d['fragment_mass'],
                        data_stage01_isotopomer_normalized.scan_type.like(d['scan_type'])).update(		
                        {
                        'used_':d['used_'],
                        'comment_':d['comment_']},
                        synchronize_session=False);
                if data_update == 0:
                    print('row not found.')
                    print(d)
            except SQLAlchemyError as e:
                print(e);
        self.session.commit();

    def add_dataStage01IsotopomerNormalized(self,dataListUpdated_I):
        # add to data_stage01_isotopomer_normalized
        for d in dataListUpdated_I:
            try:
                data_update = data_stage01_isotopomer_normalized(d['experiment_id'],
                        d['sample_name_abbreviation'],
                        d['time_point'],
                        d['dilution'],
                        d['sample_type'],
                        d['replicate_number'],
                        d['met_id'],
                        d['fragment_formula'],
                        d['fragment_mass'],
                        d['intensity'],
                        d['intensity_units'],
                        d['intensity_corrected'],
                        d['intensity_corrected_units'],
                        d['intensity_normalized'],
                        d['intensity_normalized_units'],
                        d['scan_type'],
                        d['used_'],
                        d['comment_']);
                self.session.add(data_add);
            except SQLAlchemyError as e:
                print(e);
        self.session.commit();