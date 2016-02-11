from .stage01_isotopomer_MQResultsTable_postgresql_models import *
from SBaaS_LIMS.lims_experiment_postgresql_models import *
from SBaaS_LIMS.lims_sample_postgresql_models import *
from SBaaS_LIMS.lims_msMethod_postgresql_models import *

from SBaaS_base.sbaas_base_query_update import sbaas_base_query_update
from SBaaS_base.sbaas_base_query_drop import sbaas_base_query_drop
from SBaaS_base.sbaas_base_query_initialize import sbaas_base_query_initialize
from SBaaS_base.sbaas_base_query_insert import sbaas_base_query_insert
from SBaaS_base.sbaas_base_query_select import sbaas_base_query_select
from SBaaS_base.sbaas_base_query_delete import sbaas_base_query_delete

from SBaaS_base.sbaas_template_query import sbaas_template_query

class stage01_isotopomer_MQResultsTable_query(sbaas_template_query):
    def initialize_supportedTables(self):
        '''Set the supported tables dict for 
        '''
        tables_supported = {'data_stage01_isotopomer_mqresultstable':data_stage01_isotopomer_mqresultstable,
                        };
        self.set_supportedTables(tables_supported);
    def initialize_dataStage01_isotopomer_MQResultsTable(self):
        try:
            data_stage01_isotopomer_MQResultsTable.__table__.create(self.engine,True);
        except SQLAlchemyError as e:
            print(e);
    def drop_dataStage01_isotopomer_MQResultsTable(self):
        try:
            data_stage01_isotopomer_MQResultsTable.__table__.drop(self.engine,True);
        except SQLAlchemyError as e:
            print(e);
    # query sample names from data_stage01_isotopomer_mqresultstable
    def get_sampleNames_experimentIDAndSampleType(self,experiment_id_I,sample_type_I,exp_type_I=5):
        '''Querry sample names (i.e. unknowns) that are used from
        the experiment'''
        try:
            sample_names = self.session.query(data_stage01_isotopomer_MQResultsTable.sample_name).filter(
                    data_stage01_isotopomer_MQResultsTable.sample_type.like(sample_type_I),
                    experiment.id.like(experiment_id_I),
                    experiment.exp_type_id == exp_type_I,
                    data_stage01_isotopomer_MQResultsTable.used_.is_(True),
                    experiment.sample_name.like(data_stage01_isotopomer_MQResultsTable.sample_name)).group_by(
                    data_stage01_isotopomer_MQResultsTable.sample_name).order_by(
                    data_stage01_isotopomer_MQResultsTable.sample_name.asc()).all();
            sample_names_O = [];
            for sn in sample_names: sample_names_O.append(sn.sample_name);
            return sample_names_O;
        except SQLAlchemyError as e:
            print(e);
    def get_allSampleNames_experimentIDAndSampleType(self,experiment_id_I,sample_type_I,exp_type_I=5):
        '''Querry sample names (i.e. unknowns) that are used from
        the experiment'''
        try:
            sample_names = self.session.query(data_stage01_isotopomer_MQResultsTable.sample_name).filter(
                    data_stage01_isotopomer_MQResultsTable.sample_type.like(sample_type_I),
                    experiment.id.like(experiment_id_I),
                    experiment.exp_type_id == exp_type_I,
                    experiment.sample_name.like(data_stage01_isotopomer_MQResultsTable.sample_name)).group_by(
                    data_stage01_isotopomer_MQResultsTable.sample_name).order_by(
                    data_stage01_isotopomer_MQResultsTable.sample_name.asc()).all();
            sample_names_O = [];
            for sn in sample_names: sample_names_O.append(sn.sample_name);
            return sample_names_O;
        except SQLAlchemyError as e:
            print(e);
    def get_sampleNames_experimentIDAndSampleID(self,experiment_id_I,sample_id_I,exp_type_I=5):
        '''Querry sample names (i.e. unknowns) that are used from
        the experiment'''
        try:
            sample_names = self.session.query(sample.sample_name).filter(
                    sample.sample_id.like(sample_id_I),
                    experiment.id.like(experiment_id_I),
                    experiment.exp_type_id == exp_type_I,
                    data_stage01_isotopomer_MQResultsTable.used_.is_(True),
                    experiment.sample_name.like(sample.sample_name),
                    experiment.sample_name.like(data_stage01_isotopomer_MQResultsTable.sample_name)).group_by(
                    sample.sample_name).order_by(
                    sample.sample_name.asc()).all();
            sample_names_O = [];
            for sn in sample_names: sample_names_O.append(sn.sample_name);
            return sample_names_O;
        except SQLAlchemyError as e:
            print(e);
    def get_sampleNames_experimentIDAndSampleIDAndSampleDilution(self,experiment_id_I,sample_id_I,sample_dilution_I,exp_type_I=5):
        '''Querry sample names (i.e. unknowns) that are used from
        the experiment'''
        try:
            sample_names = self.session.query(sample.sample_name).filter(
                    sample.sample_id.like(sample_id_I),
                    sample.sample_dilution == sample_dilution_I,
                    experiment.id.like(experiment_id_I),
                    experiment.exp_type_id == exp_type_I,
                    data_stage01_isotopomer_MQResultsTable.used_.is_(True),
                    experiment.sample_name.like(sample.sample_name),
                    experiment.sample_name.like(data_stage01_isotopomer_MQResultsTable.sample_name)).group_by(
                    sample.sample_name).order_by(
                    sample.sample_name.asc()).all();
            sample_names_O = [];
            for sn in sample_names: sample_names_O.append(sn.sample_name);
            return sample_names_O;
        except SQLAlchemyError as e:
            print(e);
    def get_sampleNames_experimentIDAndSampleNameShortAndSampleDescription(self,experiment_id_I,sample_name_short_I,sample_decription_I,exp_type_I=5):
        '''Querry sample names that are used from
        the experiment'''
        try:
            sample_names = self.session.query(sample.sample_name).filter(
                    sample_description.sample_name_short.like(sample_name_short_I),
                    sample_description.sample_desc.like(sample_decription_I),
                    experiment.id.like(experiment_id_I),
                    experiment.exp_type_id == exp_type_I,
                    sample.sample_id.like(sample_description.sample_id),
                    experiment.sample_name.like(sample.sample_name),
                    experiment.sample_name.like(data_stage01_isotopomer_MQResultsTable.sample_name),
                    data_stage01_isotopomer_MQResultsTable.used_.is_(True)).group_by(
                    sample.sample_name).order_by(
                    sample.sample_name.asc()).all();
            sample_names_O = [];
            for sn in sample_names: sample_names_O.append(sn.sample_name);
            return sample_names_O;
        except SQLAlchemyError as e:
            print(e);
    def get_sampleNames_experimentIDAndSampleNameAbbreviationAndSampleDescription(self,experiment_id_I,sample_name_abbreviation_I,sample_decription_I,exp_type_I=5):
        '''Querry sample names that are used from
        the experiment'''
        try:
            sample_names = self.session.query(sample.sample_name).filter(
                    sample_description.sample_name_abbreviation.like(sample_name_abbreviation_I),
                    sample_description.sample_desc.like(sample_decription_I),
                    experiment.id.like(experiment_id_I),
                    experiment.exp_type_id == exp_type_I,
                    sample.sample_id.like(sample_description.sample_id),
                    experiment.sample_name.like(sample.sample_name),
                    experiment.sample_name.like(data_stage01_isotopomer_MQResultsTable.sample_name),
                    data_stage01_isotopomer_MQResultsTable.used_.is_(True)).group_by(
                    sample.sample_name).order_by(
                    sample.sample_name.asc()).all();
            sample_names_O = [];
            for sn in sample_names: sample_names_O.append(sn.sample_name);
            return sample_names_O;
        except SQLAlchemyError as e:
            print(e);
    def get_sampleNames_experimentIDAndSampleNameAbbreviationAndSampleDilution(self,experiment_id_I,sample_name_abbreviation_I,sample_dilution_I,exp_type_I=5):
        '''Querry sample names that are used from
        the experiment'''
        try:
            sample_names = self.session.query(sample.sample_name).filter(
                    sample_description.sample_name_abbreviation.like(sample_name_abbreviation_I),
                    sample.sample_dilution == sample_dilution_I,
                    experiment.id.like(experiment_id_I),
                    experiment.exp_type_id == exp_type_I,
                    sample.sample_id.like(sample_description.sample_id),
                    experiment.sample_name.like(sample.sample_name),
                    experiment.sample_name.like(data_stage01_isotopomer_MQResultsTable.sample_name),
                    data_stage01_isotopomer_MQResultsTable.used_.is_(True)).group_by(
                    sample.sample_name).order_by(
                    sample.sample_name.asc()).all();
            sample_names_O = [];
            for sn in sample_names: sample_names_O.append(sn.sample_name);
            return sample_names_O;
        except SQLAlchemyError as e:
            print(e);
    def get_sampleNamesAndReplicateNumbersAndSampleTypes_experimentIDAndSampleNameAbbreviationAndSampleDescriptionAndComponentNameAndTimePointAndDilution(\
        self,experiment_id_I,sample_name_abbreviation_I,sample_description_I,component_name_I,time_point_I,sample_dilution_I,exp_type_I=5):
        '''Querry sample names that are used from
        the experiment'''
        try:
            sample_names = self.session.query(sample.sample_name,
                    sample_description.sample_replicate,
                    sample.sample_type).filter(
                    sample_description.sample_name_abbreviation.like(sample_name_abbreviation_I),
                    sample_description.time_point.like(time_point_I),
                    sample_description.sample_desc.like(sample_description_I),
                    sample.sample_id.like(sample_description.sample_id),
                    sample.sample_dilution == sample_dilution_I,
                    experiment.sample_name.like(sample.sample_name),
                    experiment.id.like(experiment_id_I),
                    experiment.exp_type_id == exp_type_I,
                    experiment.sample_name.like(data_stage01_isotopomer_MQResultsTable.sample_name),
                    data_stage01_isotopomer_MQResultsTable.component_name.like(component_name_I),
                    data_stage01_isotopomer_MQResultsTable.used_.is_(True)).group_by(
                    sample.sample_name,
                    sample_description.sample_replicate,
                    sample.sample_type).order_by(
                    sample.sample_name.asc()).all();
            sample_names_O = [];
            sample_replicates_O = [];
            sample_types_O = [];
            for sn in sample_names:
                sample_names_O.append(sn.sample_name);
                sample_replicates_O.append(sn.sample_replicate);
                sample_types_O.append(sn.sample_type);
            return sample_names_O,sample_replicates_O,sample_types_O;
        except SQLAlchemyError as e:
            print(e);
    def get_sampleNamesAndReplicateNumbersAndSampleTypes_experimentIDAndSampleNameAbbreviationAndSampleDescriptionAndTimePointAndDilution(\
        self,experiment_id_I,sample_name_abbreviation_I,sample_description_I,time_point_I,sample_dilution_I,exp_type_I=5):
        '''Querry sample names that are used from
        the experiment'''
        try:
            sample_names = self.session.query(sample.sample_name,
                    sample_description.sample_replicate,
                    sample.sample_type).filter(
                    sample_description.sample_name_abbreviation.like(sample_name_abbreviation_I),
                    sample_description.time_point.like(time_point_I),
                    sample_description.sample_desc.like(sample_description_I),
                    sample.sample_id.like(sample_description.sample_id),
                    sample.sample_dilution == sample_dilution_I,
                    experiment.sample_name.like(sample.sample_name),
                    experiment.id.like(experiment_id_I),
                    experiment.exp_type_id == exp_type_I,
                    experiment.sample_name.like(data_stage01_isotopomer_MQResultsTable.sample_name),
                    data_stage01_isotopomer_MQResultsTable.used_.is_(True)).group_by(
                    sample.sample_name,
                    sample_description.sample_replicate,
                    sample.sample_type).order_by(
                    sample.sample_name.asc()).all();
            sample_names_O = [];
            sample_replicates_O = [];
            sample_types_O = [];
            for sn in sample_names:
                sample_names_O.append(sn.sample_name);
                sample_replicates_O.append(sn.sample_replicate);
                sample_types_O.append(sn.sample_type);
            return sample_names_O,sample_replicates_O,sample_types_O;
        except SQLAlchemyError as e:
            print(e);
    # query sample ids from data_stage01_isotopomer_mqresultstable
    def get_sampleIDs_experimentIDAndSampleType(self,experiment_id_I,sample_type_I,exp_type_I=5):
        '''Querry sample names (i.e. unknowns) that are used from
        the experiment'''
        try:
            sample_ids = self.session.query(sample.sample_id).filter(
                    data_stage01_isotopomer_MQResultsTable.sample_type.like(sample_type_I),
                    experiment.id.like(experiment_id_I),
                    experiment.exp_type_id == exp_type_I,
                    data_stage01_isotopomer_MQResultsTable.used_.is_(True),
                    experiment.sample_name.like(sample.sample_name),
                    experiment.sample_name.like(data_stage01_isotopomer_MQResultsTable.sample_name)).group_by(
                    sample.sample_id).order_by(
                    sample.sample_id.asc()).all();
            sample_ids_O = [];
            for si in sample_ids: sample_ids_O.append(si.sample_id);
            return sample_ids_O;
        except SQLAlchemyError as e:
            print(e);
    def get_sampleIDs_experimentID(self,experiment_id_I,exp_type_I=5):
        '''Querry sample names that are used from the experiment'''
        try:
            sample_ids = self.session.query(sample.sample_id).filter(
                    experiment.id.like(experiment_id_I),
                    experiment.exp_type_id == exp_type_I,
                    data_stage01_isotopomer_MQResultsTable.used_.is_(True),
                    experiment.sample_name.like(sample.sample_name),
                    experiment.sample_name.like(data_stage01_isotopomer_MQResultsTable.sample_name)).group_by(
                    sample.sample_id).order_by(
                    sample.sample_id.asc()).all();
            sample_ids_O = [];
            for si in sample_ids: sample_ids_O.append(si.sample_id);
            return sample_ids_O;
        except SQLAlchemyError as e:
            print(e);
    def get_sampleID_experimentIDAndSampleName(self,experiment_id_I,sample_name_I,exp_type_I=5):
        '''Querry sample names (i.e. unknowns) that are used from
        the experiment'''
        try:
            sample_id = self.session.query(sample.sample_id).filter(
                    sample.sample_name.like(sample_name_I),
                    experiment.id.like(experiment_id_I),
                    experiment.exp_type_id == exp_type_I,
                    data_stage01_isotopomer_MQResultsTable.used_.is_(True),
                    experiment.sample_name.like(sample.sample_name),
                    experiment.sample_name.like(data_stage01_isotopomer_MQResultsTable.sample_name)).group_by(
                    sample.sample_id).all();
            sample_id_O = sample_id[0];
            return sample_id_O;
        except SQLAlchemyError as e:
            print(e);
    # query sample names and sample name short
    def get_sampleNamesAndShortName_experimentIDAndSampleTypeAndTimePointAndDilution(experiment_id_I,sample_type_I,tp,dilution_I,exp_type_I=5):
        '''Querry sample name and sample name short that are used from
        the experimentfor specific time-points and dilutions'''
        try:
            sample_name_short = self.session.query(sample.sample_name,
                    sample_description.sample_name_short).filter(
                    experiment.id.like(experiment_id_I),
                    experiment.exp_type_id == exp_type_I,
                    data_stage01_isotopomer_MQResultsTable.sample_name.like(experiment.sample_name),
                    data_stage01_isotopomer_MQResultsTable.sample_type.like(sample_type_I),
                    data_stage01_isotopomer_MQResultsTable.used_.is_(True),
                    sample.sample_name.like(experiment.sample_name),
                    sample.sample_type.like(sample_type_I),
                    sample.sample_dilution == dilution_I,
                    sample_description.sample_id.like(sample.sample_id),
                    sample_description.time_point.like(time_point_I)).group_by(
                    sample.sample_name).order_by(
                    sample.sample_name).all();
            sample_name_O = [];
            sample_name_short_O = [];
            for sn in sample_name_short:
                sample_name_O.append(sn.sample_name);
                sample_name_short_O.append(sn.sample_name_short);
            return sample_name_short_O;
        except SQLAlchemyError as e:
            print(e);
    # query sample names and sample name abbreviations
    def get_sampleNamesAndAbbreviations_experimentIDAndSampleTypeAndTimePointAndDilution(experiment_id_I,sample_type_I,tp,dilution_I,exp_type_I=5):
        '''Querry sample name and sample abbreviation that are used from
        the experimentfor specific time-points and dilutions'''
        try:
            sample_name_abbreviation = self.session.query(sample.sample_name,
                    sample_description.sample_name_abbreviation).filter(
                    experiment.id.like(experiment_id_I),
                    experiment.exp_type_id == exp_type_I,
                    data_stage01_isotopomer_MQResultsTable.sample_name.like(experiment.sample_name),
                    data_stage01_isotopomer_MQResultsTable.sample_type.like(sample_type_I),
                    data_stage01_isotopomer_MQResultsTable.used_.is_(True),
                    sample.sample_name.like(experiment.sample_name),
                    sample.sample_type.like(sample_type_I),
                    sample.sample_dilution == dilution_I,
                    sample_description.sample_id.like(sample.sample_id),
                    sample_description.time_point.like(time_point_I)).group_by(
                    sample.sample_name).order_by(
                    sample.sample_name).all();
            sample_name_O = [];
            sample_name_abbreviation_O = [];
            for sn in sample_name_abbreviation:
                sample_name_O.append(sn.sample_name);
                sample_name_abbreviation_O.append(sn.sample_name_abbreviation);
            return sample_name_O, sample_name_abbreviation_O;
        except SQLAlchemyError as e:
            print(e);
    # query sample name short from data_stage01_isotopomer_mqresultstable
    def get_sampleNameShort_experimentIDAndSampleType(self,experiment_id_I,sample_type_I,exp_type_I=5):
        '''Querry sample name short that are used from
        the experiment'''
        try:
            sample_name_short = self.session.query(sample_description.sample_name_short).filter(
                    sample.sample_type.like(sample_type_I),
                    experiment.exp_type_id == exp_type_I,
                    experiment.id.like(experiment_id_I),
                    data_stage01_isotopomer_MQResultsTable.used_.is_(True),
                    experiment.sample_name.like(sample.sample_name),
                    sample.sample_id.like(sample_description.sample_id),
                    experiment.sample_name.like(data_stage01_isotopomer_MQResultsTable.sample_name)).group_by(
                    sample_description.sample_name_short).order_by(
                    sample_description.sample_name_short.asc()).all();
            sample_name_short_O = [];
            for sns in sample_name_short: sample_name_short_O.append(sns.sample_name_short);
            return sample_name_short_O;
        except SQLAlchemyError as e:
            print(e);
    def get_sampleNameShort_experimentIDAndSampleName(self,experiment_id_I,sample_name_I,exp_type_I=5):
        '''Querry sample name short that are used from
        the experiment'''
        try:
            sample_name_short = self.session.query(sample_description.sample_name_short).filter(
                    sample.sample_name.like(sample_name_I),
                    experiment.id.like(experiment_id_I),
                    experiment.exp_type_id == exp_type_I,
                    data_stage01_isotopomer_MQResultsTable.used_.is_(True),
                    experiment.sample_name.like(sample.sample_name),
                    sample.sample_id.like(sample_description.sample_id),
                    experiment.sample_name.like(data_stage01_isotopomer_MQResultsTable.sample_name)).group_by(
                    sample_description.sample_name_short).all();
            sample_name_short_O = sample_name_short[0];
            return sample_name_short_O;
        except SQLAlchemyError as e:
            print(e);
    # query sample name abbreviations from data_stage01_isotopomer_mqresultstable
    def get_sampleNameAbbreviations_experimentID(self,experiment_id_I,exp_type_I=5):
        '''Querry sample name abbreviations that are used from
        the experiment'''
        try:
            sample_name_abbreviations = self.session.query(sample_description.sample_name_abbreviation).filter(
                    experiment.id.like(experiment_id_I),
                    experiment.exp_type_id == exp_type_I,
                    data_stage01_isotopomer_MQResultsTable.used_.is_(True),
                    experiment.sample_name.like(sample.sample_name),
                    sample.sample_id.like(sample_description.sample_id),
                    experiment.sample_name.like(data_stage01_isotopomer_MQResultsTable.sample_name)).group_by(
                    sample_description.sample_name_abbreviation).order_by(
                    sample_description.sample_name_abbreviation.asc()).all();
            sample_name_abbreviations_O = [];
            for sna in sample_name_abbreviations: sample_name_abbreviations_O.append(sna.sample_name_abbreviation);
            return sample_name_abbreviations_O;
        except SQLAlchemyError as e:
            print(e);
    def get_sampleNameAbbreviations_experimentIDAndSampleType(self,experiment_id_I,sample_type_I,exp_type_I=5):
        '''Querry sample name abbreviations that are used from
        the experiment'''
        try:
            sample_name_abbreviations = self.session.query(sample_description.sample_name_abbreviation).filter(
                    sample.sample_type.like(sample_type_I),
                    experiment.exp_type_id == exp_type_I,
                    experiment.id.like(experiment_id_I),
                    data_stage01_isotopomer_MQResultsTable.used_.is_(True),
                    experiment.sample_name.like(sample.sample_name),
                    sample.sample_id.like(sample_description.sample_id),
                    experiment.sample_name.like(data_stage01_isotopomer_MQResultsTable.sample_name)).group_by(
                    sample_description.sample_name_abbreviation).order_by(
                    sample_description.sample_name_abbreviation.asc()).all();
            sample_name_abbreviations_O = [];
            for sna in sample_name_abbreviations: sample_name_abbreviations_O.append(sna.sample_name_abbreviation);
            return sample_name_abbreviations_O;
        except SQLAlchemyError as e:
            print(e);
    def get_sampleNameAbbreviations_experimentIDAndSampleName(self,experiment_id_I,sample_name_I,exp_type_I=5):
        '''Querry sample name abbreviations that are used from
        the experiment by sample name'''
        try:
            sample_name_abbreviations = self.session.query(sample_description.sample_name_abbreviation).filter(
                    sample.sample_name.like(sample_name_I),
                    experiment.id.like(experiment_id_I),
                    experiment.exp_type_id == exp_type_I,
                    data_stage01_isotopomer_MQResultsTable.used_.is_(True),
                    experiment.sample_name.like(sample.sample_name),
                    sample.sample_id.like(sample_description.sample_id),
                    experiment.sample_name.like(data_stage01_isotopomer_MQResultsTable.sample_name)).group_by(
                    sample_description.sample_name_abbreviation).order_by(
                    sample_description.sample_name_abbreviation.asc()).all();
            sample_name_abbreviations_O = [];
            for sna in sample_name_abbreviations: sample_name_abbreviations_O.append(sna.sample_name_abbreviation);
            return sample_name_abbreviations_O;
        except SQLAlchemyError as e:
            print(e);
    def get_sampleNameAbbreviations_experimentIDAndSampleTypeAndTimePointAndDilution(self,experiment_id_I,sample_type_I,time_point_I,dilution_I,exp_type_I=5):
        '''Querry sample name abbreviations that are used from
        the experiment for specific time-points and dilutions'''
        try:
            sample_name_abbreviations = self.session.query(
                    sample_description.sample_name_abbreviation).filter(
                    experiment.id.like(experiment_id_I),
                    experiment.exp_type_id == exp_type_I,
                    data_stage01_isotopomer_MQResultsTable.sample_name.like(experiment.sample_name),
                    data_stage01_isotopomer_MQResultsTable.used_.is_(True),
                    sample.sample_name.like(experiment.sample_name),
                    sample.sample_type.like(sample_type_I),
                    sample.sample_dilution == dilution_I,
                    sample_description.sample_id.like(sample.sample_id),
                    sample_description.time_point.like(time_point_I)).group_by(
                    sample_description.sample_name_abbreviation).order_by(
                    sample_description.sample_name_abbreviation).all();
            sample_name_abbreviations_O = [];
            for sn in sample_name_abbreviations:
                sample_name_abbreviations_O.append(sn[0]);
            return sample_name_abbreviations_O;
        except SQLAlchemyError as e:
            print(e);
    # query dilutions from data_stage01_isotopomer_mqresultstable
    def get_sampleDilution_experimentIDAndSampleID(self,experiment_id_I,sample_id_I,exp_type_I=5):
        '''Querry dilutions that are used from the experiment'''
        try:
            sample_dilutions = self.session.query(sample.sample_dilution).filter(
                    sample.sample_id.like(sample_id_I),
                    experiment.id.like(experiment_id_I),
                    experiment.exp_type_id == exp_type_I,
                    data_stage01_isotopomer_MQResultsTable.used_.is_(True),
                    experiment.sample_name.like(sample.sample_name),
                    experiment.sample_name.like(data_stage01_isotopomer_MQResultsTable.sample_name)).group_by(
                    sample.sample_dilution).order_by(
                    sample.sample_dilution.asc()).all();
            sample_dilutions_O = [];
            for sd in sample_dilutions: sample_dilutions_O.append(sd.sample_dilution);
            return sample_dilutions_O;
        except SQLAlchemyError as e:
            print(e);
    def get_sampleDilution_experimentIDAndSampleNameAbbreviation(self,experiment_id_I,sample_name_abbreviation_I,exp_type_I=5):
        '''Querry dilutions that are used from the experiment'''
        try:
            sample_dilutions = self.session.query(sample.sample_dilution).filter(
                    experiment.id.like(experiment_id_I),
                    experiment.exp_type_id == exp_type_I,
                    experiment.sample_name.like(sample.sample_name),
                    sample.sample_id.like(sample_description.sample_id),
                    sample_description.sample_name_abbreviation.like(sample_name_abbreviation_I),
                    data_stage01_isotopomer_MQResultsTable.used_.is_(True),
                    experiment.sample_name.like(data_stage01_isotopomer_MQResultsTable.sample_name)).group_by(
                    sample.sample_dilution).order_by(
                    sample.sample_dilution.asc()).all();
            sample_dilutions_O = [];
            for sd in sample_dilutions: sample_dilutions_O.append(sd.sample_dilution);
            return sample_dilutions_O;
        except SQLAlchemyError as e:
            print(e);
    def get_sampleDilution_experimentIDAndTimePoint(self,experiment_id_I,time_point_I,exp_type_I=5):
        '''Querry dilutions that are used from the experiment'''
        try:
            sample_dilutions = self.session.query(sample.sample_dilution).filter(
                    experiment.id.like(experiment_id_I),
                    experiment.exp_type_id == exp_type_I,
                    experiment.sample_name.like(sample.sample_name),
                    data_stage01_isotopomer_MQResultsTable.sample_name.like(experiment.sample_name),
                    data_stage01_isotopomer_MQResultsTable.used_.is_(True),
                    sample.sample_id.like(sample_description.sample_id),
                    sample_description.time_point.like(time_point_I)).group_by(
                    sample.sample_dilution).order_by(
                    sample.sample_dilution.asc()).all();
            sample_dilutions_O = [];
            for sd in sample_dilutions: sample_dilutions_O.append(sd.sample_dilution);
            return sample_dilutions_O;
        except SQLAlchemyError as e:
            print(e);
    # query time points from data_stage01_isotopomer_mqresultstable
    def get_timePoint_experimentIDAndSampleNameAbbreviation(self,experiment_id_I,sample_name_abbreviation_I,exp_type_I=5):
        '''Querry time points that are used from the experiment and sample name abbreviation'''
        try:
            time_points = self.session.query(sample_description.time_point).filter(
                    sample_description.sample_name_abbreviation.like(sample_name_abbreviation_I),
                    experiment.id.like(experiment_id_I),
                    experiment.exp_type_id == exp_type_I,
                    data_stage01_isotopomer_MQResultsTable.used_.is_(True),
                    experiment.sample_name.like(sample.sample_name),
                    sample.sample_id.like(sample_description.sample_id),
                    experiment.sample_name.like(data_stage01_isotopomer_MQResultsTable.sample_name)).group_by(
                    sample_description.time_point).order_by(
                    sample_description.time_point.asc()).all();
            time_points_O = [];
            for tp in time_points: time_points_O.append(tp.time_point);
            return time_points_O;
        except SQLAlchemyError as e:
            print(e);
    def get_timePoint_experimentIDAndSampleName(self,experiment_id_I,sample_name_I,exp_type_I=5):
        '''Querry time points that are used from the experiment and sample name'''
        try:
            time_points = self.session.query(sample_description.time_point).filter(
                    experiment.id.like(experiment_id_I),
                    experiment.exp_type_id == exp_type_I,
                    experiment.sample_name.like(sample_name_I),
                    experiment.sample_name.like(sample.sample_name),
                    data_stage01_isotopomer_MQResultsTable.sample_name.like(experiment.sample_name),
                    data_stage01_isotopomer_MQResultsTable.used_.is_(True),
                    sample.sample_id.like(sample_description.sample_id)).group_by(
                    sample_description.time_point).order_by(
                    sample_description.time_point.asc()).all();
            time_points_O = [];
            for tp in time_points: time_points_O.append(tp.time_point);
            return time_points_O;
        except SQLAlchemyError as e:
            print(e);
    def get_timePoint_experimentID(self,experiment_id_I,exp_type_I=5):
        '''Querry time points that are used from the experiment and sample name'''
        try:
            time_points = self.session.query(sample_description.time_point).filter(
                    experiment.id.like(experiment_id_I),
                    experiment.exp_type_id == exp_type_I,
                    experiment.sample_name.like(sample.sample_name),
                    data_stage01_isotopomer_MQResultsTable.sample_name.like(experiment.sample_name),
                    data_stage01_isotopomer_MQResultsTable.used_.is_(True),
                    sample.sample_id.like(sample_description.sample_id)).group_by(
                    sample_description.time_point).order_by(
                    sample_description.time_point.asc()).all();
            time_points_O = [];
            for tp in time_points: time_points_O.append(tp.time_point);
            return time_points_O;
        except SQLAlchemyError as e:
            print(e);
    # query component names from data_stage01_isotopomer_mqresultstable
    def get_componentsNames_experimentIDAndSampleID(self,experiment_id_I,sample_id_I,exp_type_I=5):
        '''Querry component names that are used and are not IS from
        the experiment and sample_id'''
        try:
            component_names = self.session.query(data_stage01_isotopomer_MQResultsTable.component_name).filter(
                    experiment.id.like(experiment_id_I),
                    experiment.exp_type_id == exp_type_I,
                    data_stage01_isotopomer_MQResultsTable.used_.is_(True),                   
                    data_stage01_isotopomer_MQResultsTable.is_.is_(False),
                    experiment.sample_name.like(sample.sample_name),
                    sample.sample_id.like(sample_id_I),
                    experiment.sample_name.like(data_stage01_isotopomer_MQResultsTable.sample_name)).group_by(
                    data_stage01_isotopomer_MQResultsTable.component_name).order_by(
                    data_stage01_isotopomer_MQResultsTable.component_name.asc()).all();
            component_names_O = [];
            for cn in component_names: component_names_O.append(cn.component_name);
            return component_names_O;
        except SQLAlchemyError as e:
            print(e);
    def get_componentsNames_experimentIDAndSampleNameAbbreviation(self,experiment_id_I,sample_name_abbreviation_I,exp_type_I=5):
        '''Querry component names that are used from
        the experiment and sample_name_abbreviation'''
        try:
            component_names = self.session.query(data_stage01_isotopomer_MQResultsTable.component_name).filter(
                    sample_description.sample_name_abbreviation.like(sample_name_abbreviation_I),
                    experiment.id.like(experiment_id_I),
                    experiment.exp_type_id == exp_type_I,
                    sample.sample_id.like(sample_description.sample_id),
                    experiment.sample_name.like(sample.sample_name),
                    experiment.sample_name.like(data_stage01_isotopomer_MQResultsTable.sample_name),                   
                    data_stage01_isotopomer_MQResultsTable.used_.is_(True),                   
                    data_stage01_isotopomer_MQResultsTable.is_.is_(False)).group_by(
                    data_stage01_isotopomer_MQResultsTable.component_name).order_by(
                    data_stage01_isotopomer_MQResultsTable.component_name.asc()).all();
            component_names_O = [];
            for cn in component_names: component_names_O.append(cn.component_name);
            return component_names_O;
        except SQLAlchemyError as e:
            print(e);
    def get_componentsNames_experimentIDAndSampleName(self,experiment_id_I,sample_name_I,exp_type_I=5):
        '''Querry component names that are used and not internal standards from
        the experiment and sample_name'''
        try:
            component_names = self.session.query(data_stage01_isotopomer_MQResultsTable.component_name).filter(
                    experiment.sample_name.like(sample_name_I),
                    experiment.id.like(experiment_id_I),
                    experiment.exp_type_id == exp_type_I,
                    experiment.sample_name.like(data_stage01_isotopomer_MQResultsTable.sample_name),                   
                    data_stage01_isotopomer_MQResultsTable.used_.is_(True),                   
                    data_stage01_isotopomer_MQResultsTable.is_.is_(False)).group_by(
                    data_stage01_isotopomer_MQResultsTable.component_name).order_by(
                    data_stage01_isotopomer_MQResultsTable.component_name.asc()).all();
            component_names_O = [];
            for cn in component_names: component_names_O.append(cn.component_name);
            return component_names_O;
        except SQLAlchemyError as e:
            print(e);
    # query component group names from data_stage01_isotopomer_mqresultstable
    def get_componentGroupNames_sampleName(self,sample_name_I):
        '''Querry component group names that are used from the sample name
        NOTE: intended to be used within a for loop'''
        try:
            component_group_names = self.session.query(data_stage01_isotopomer_MQResultsTable.component_group_name).filter(
                    data_stage01_isotopomer_MQResultsTable.sample_name.like(sample_name_I)).group_by(
                    data_stage01_isotopomer_MQResultsTable.component_group_name).order_by(
                    data_stage01_isotopomer_MQResultsTable.component_group_name.asc()).all();
            component_group_names_O = [];
            for cgn in component_group_names: component_group_names_O.append(cgn.component_group_name);
            return component_group_names_O;
        except SQLAlchemyError as e:
            print(e);
    def get_componentGroupName_experimentIDAndComponentName(self,experiment_id_I,component_name_I,exp_type_I=5):
        '''Querry component group names that are used from the component name
        NOTE: intended to be used within a for loop'''
        try:
            component_group_name = self.session.query(data_stage01_isotopomer_MQResultsTable.component_group_name).filter(
                    experiment.id.like(experiment_id_I),
                    experiment.exp_type_id == exp_type_I,
                    experiment.sample_name.like(data_stage01_isotopomer_MQResultsTable.sample_name),
                    data_stage01_isotopomer_MQResultsTable.component_name.like(component_name_I)).group_by(
                    data_stage01_isotopomer_MQResultsTable.component_group_name).all();
            if len(component_group_name)>1:
                print('more than 1 component_group_name retrieved per component_name')
            component_group_name_O = component_group_name[0];
            return component_group_name_O;
        except SQLAlchemyError as e:
            print(e);
    # query component names, group names, intensity,
    #   precursor formula, product formula, precursor mass, product mass
    def get_componentsNamesAndData_experimentIDAndSampleNameAndMSMethodType(self,experiment_id_I,sample_name_I,ms_methodtype_I,exp_type_I=5):
        '''Querry component names, group names, fragment formula, and fragment mass
        that are used the experiment and sample_name'''
        try:
            component_names = self.session.query(data_stage01_isotopomer_MQResultsTable.component_name,
                    data_stage01_isotopomer_MQResultsTable.component_group_name,
                    data_stage01_isotopomer_MQResultsTable.height, #peak height
                    MS_components.precursor_formula,
                    MS_components.precursor_exactmass,
                    MS_components.product_formula,
                    MS_components.product_exactmass).filter(
                    data_stage01_isotopomer_MQResultsTable.sample_name.like(sample_name_I),               
                    data_stage01_isotopomer_MQResultsTable.used_.is_(True),
                    experiment.id.like(experiment_id_I),
                    experiment.exp_type_id == exp_type_I,
                    experiment.sample_name.like(data_stage01_isotopomer_MQResultsTable.sample_name),
                    MS_components.component_name.like(data_stage01_isotopomer_MQResultsTable.component_name),
                    MS_components.ms_methodtype.like(ms_methodtype_I)).group_by(
                    data_stage01_isotopomer_MQResultsTable.component_name).order_by(
                    data_stage01_isotopomer_MQResultsTable.component_name.asc()).all();
            component_names_O = [];
            component_group_names_O = [];
            intensities_O = [];
            precursor_formulas_O = [];
            precursor_masses_O = [];
            product_formulas_O = [];
            product_masses_O = [];
            for cn in component_names:
                component_names_O.append(cn.component_name);
                component_group_names_O.append(cn. component_group_name);
                intensities_O.append(cn.height);
                precursor_formulas_O.append(cn.precursor_formula);
                precursor_masses_O.append(cn.precursor_exactmass);
                product_formulas_O.append(cn.product_formula);
                product_masses_O.append(cn.product_exactmass);
            return component_names_O, component_group_names_O, intensities_O,\
                    precursor_formulas_O, precursor_masses_O, product_formulas_O, product_masses_O;
        except SQLAlchemyError as e:
            print(e);
    # query component names, group names, precursor formula, product formula, precursor mass, product mass
    def get_componentsNamesAndOther_experimentIDAndSampleNameAndMSMethodTypeAndTimePointAndDilution(self,experiment_id_I,sample_name_abbreviation_I,ms_methodtype_I,time_point_I,dilution_I,exp_type_I=5):
        '''Querry component names, group names, fragment formula, and fragment mass
        that are used the experiment'''
        try:
            component_names = self.session.query(data_stage01_isotopomer_MQResultsTable.component_name,
                    data_stage01_isotopomer_MQResultsTable.component_group_name,
                    MS_components.precursor_formula,
                    MS_components.precursor_exactmass,
                    MS_components.product_formula,
                    MS_components.product_exactmass).filter(
                    sample_description.sample_name_abbreviation.like(sample_name_abbreviation_I),
                    sample_description.time_point.like(time_point_I),
                    sample.sample_id.like(sample_description.sample_id),
                    sample.sample_dilution == dilution_I,
                    experiment.sample_name.like(sample.sample_name),
                    experiment.id.like(experiment_id_I),
                    experiment.exp_type_id == exp_type_I,
                    data_stage01_isotopomer_MQResultsTable.sample_name.like(experiment.sample_name),               
                    data_stage01_isotopomer_MQResultsTable.used_.is_(True),
                    MS_components.component_name.like(data_stage01_isotopomer_MQResultsTable.component_name),
                    MS_components.ms_methodtype.like(ms_methodtype_I)).group_by(
                    data_stage01_isotopomer_MQResultsTable.component_name,
                    data_stage01_isotopomer_MQResultsTable.component_group_name,
                    MS_components.precursor_formula,
                    MS_components.precursor_exactmass,
                    MS_components.product_formula,
                    MS_components.product_exactmass).order_by(
                    data_stage01_isotopomer_MQResultsTable.component_name.asc()).all();
            component_names_O = [];
            component_group_names_O = [];
            precursor_formulas_O = [];
            precursor_masses_O = [];
            product_formulas_O = [];
            product_masses_O = [];
            if not component_names: 
                print('No component information found for:');
                print('experiment_id\tsample_name_abbreviation\tms_methodtype\ttime_point,dilution');
                print(experiment_id_I,sample_name_abbreviation_I,ms_methodtype_I,time_point_I,dilution_I);
                return component_names_O, component_group_names_O,\
                        precursor_formulas_O, precursor_masses_O, product_formulas_O, product_masses_O;
            else:
                for cn in component_names:
                    component_names_O.append(cn.component_name);
                    component_group_names_O.append(cn. component_group_name);
                    precursor_formulas_O.append(cn.precursor_formula);
                    precursor_masses_O.append(cn.precursor_exactmass);
                    product_formulas_O.append(cn.product_formula);
                    product_masses_O.append(cn.product_exactmass);
                return component_names_O, component_group_names_O,\
                        precursor_formulas_O, precursor_masses_O, product_formulas_O, product_masses_O;
        except SQLAlchemyError as e:
            print(e);
    # query component names, group names, precursor formula, product formula, precursor mass, product mass
    def get_componentsNamesAndOther_experimentIDAndSampleNameAndMSMethodTypeAndTimePointAndDilutionAndMetID(self,experiment_id_I,sample_name_abbreviation_I,ms_methodtype_I,time_point_I,dilution_I,met_id_I,exp_type_I=5):
        '''Querry component names, group names, fragment formula, and fragment mass
        that are used the experiment'''
        try:
            component_names = self.session.query(data_stage01_isotopomer_MQResultsTable.component_name,
                    data_stage01_isotopomer_MQResultsTable.component_group_name,
                    MS_components.precursor_formula,
                    MS_components.precursor_exactmass,
                    MS_components.product_formula,
                    MS_components.product_exactmass).filter(
                    sample_description.sample_name_abbreviation.like(sample_name_abbreviation_I),
                    sample_description.time_point.like(time_point_I),
                    sample.sample_id.like(sample_description.sample_id),
                    sample.sample_dilution == dilution_I,
                    experiment.sample_name.like(sample.sample_name),
                    experiment.id.like(experiment_id_I),
                    experiment.exp_type_id == exp_type_I,
                    data_stage01_isotopomer_MQResultsTable.sample_name.like(experiment.sample_name),      
                    data_stage01_isotopomer_MQResultsTable.used_.is_(True),
                    MS_components.component_name.like(data_stage01_isotopomer_MQResultsTable.component_name),
                    MS_components.ms_methodtype.like(ms_methodtype_I),
                    MS_components.met_id.like(met_id_I)).group_by(
                    data_stage01_isotopomer_MQResultsTable.component_name,
                    data_stage01_isotopomer_MQResultsTable.component_group_name,
                    MS_components.precursor_formula,
                    MS_components.precursor_exactmass,
                    MS_components.product_formula,
                    MS_components.product_exactmass).order_by(
                    data_stage01_isotopomer_MQResultsTable.component_name.asc()).all();
            component_names_O = [];
            component_group_names_O = [];
            precursor_formulas_O = [];
            precursor_masses_O = [];
            product_formulas_O = [];
            product_masses_O = [];
            #component_names_O = None;
            #component_group_names_O = None;
            #precursor_formulas_O = None;
            #precursor_masses_O = None;
            #product_formulas_O = None;
            #product_masses_O = None;
            if not component_names: 
                print('No component information found for:');
                print('experiment_id\tsample_name_abbreviation\tms_methodtype\ttime_point\tdilution\tmet_id');
                print(experiment_id_I,sample_name_abbreviation_I,ms_methodtype_I,time_point_I,dilution_I,met_id_I);
                return component_names_O, component_group_names_O,\
                        precursor_formulas_O, precursor_masses_O, product_formulas_O, product_masses_O;
            else:
                for cn in component_names:
                    component_names_O.append(cn.component_name);
                    component_group_names_O.append(cn. component_group_name);
                    precursor_formulas_O.append(cn.precursor_formula);
                    precursor_masses_O.append(cn.precursor_exactmass);
                    product_formulas_O.append(cn.product_formula);
                    product_masses_O.append(cn.product_exactmass);
                #component_names_O=component_names[0][0];
                #component_group_names_O=component_names[0][1];
                #precursor_formulas_O=component_names[0][2];
                #precursor_masses_O=component_names[0][3];
                #product_formulas_O=component_names[0][4];
                #product_masses_O=component_names[0][5];
                return component_names_O, component_group_names_O,\
                        precursor_formulas_O, precursor_masses_O, product_formulas_O, product_masses_O;
        except SQLAlchemyError as e:
            print(e);
    # query physiological parameters from data_stage01_isotopomer_mqresultstable
    def get_CVSAndCVSUnitsAndODAndDilAndDilUnits_sampleName(self,sample_name_I):
        '''Querry culture volume sampled, culture volume sampled units, and OD600 from sample name
        NOTE: intended to be used within a for loop'''
        try:
            physiologicalParameters = self.session.query(sample_physiologicalParameters.culture_volume_sampled,
                    sample_physiologicalParameters.culture_volume_sampled_units,
                    sample_physiologicalParameters.od600,
                    sample_description.reconstitution_volume,
                    sample_description.reconstitution_volume_units).filter(
                    sample.sample_name.like(sample_name_I),
                    sample.sample_id.like(sample_physiologicalParameters.sample_id),
                    sample.sample_id.like(sample_description.sample_id)).all();
            cvs_O = physiologicalParameters[0][0];
            cvs_units_O = physiologicalParameters[0][1];
            od600_O = physiologicalParameters[0][2];
            dil_O = physiologicalParameters[0][3];
            dil_units_O = physiologicalParameters[0][4];
            return cvs_O, cvs_units_O, od600_O, dil_O, dil_units_O;
        except SQLAlchemyError as e:
            print(e);
    def get_CVSAndCVSUnitsAndODAndDilAndDilUnits_sampleNameShort(self,sample_name_short_I):
        '''Querry culture volume sampled, culture volume sampled units, and OD600 from sample name
        NOTE: intended to be used within a for loop'''
        try:
            physiologicalParameters = self.session.query(sample_physiologicalParameters.culture_volume_sampled,
                    sample_physiologicalParameters.culture_volume_sampled_units,
                    sample_physiologicalParameters.od600,
                    sample_description.reconstitution_volume,
                    sample_description.reconstitution_volume_units).filter(
                    sample_description.sample_name_short.like(sample_name_short_I),
                    sample_description.sample_id.like(sample_physiologicalParameters.sample_id)).all();
            cvs_O = physiologicalParameters[0][0];
            cvs_units_O = physiologicalParameters[0][1];
            od600_O = physiologicalParameters[0][2];
            dil_O = physiologicalParameters[0][3];
            dil_units_O = physiologicalParameters[0][4];
            return cvs_O, cvs_units_O, od600_O, dil_O, dil_units_O;
        except SQLAlchemyError as e:
            print(e);
    def get_conversionAndConversionUnits_biologicalMaterialAndConversionName(self,biological_material_I,conversion_name_I):
        '''Querry conversion and conversion units from
        biological material and conversion name
        NOTE: intended to be used within a for loop'''
        try:
            physiologicalParameters = self.session.query(biologicalMaterial_massVolumeConversion.conversion_factor,
                    biologicalMaterial_massVolumeConversion.conversion_units).filter(
                    biologicalMaterial_massVolumeConversion.biological_material.like(biological_material_I),
                    biologicalMaterial_massVolumeConversion.conversion_name.like(conversion_name_I)).all();
            conversion_O = physiologicalParameters[0][0];
            conversion_units_O = physiologicalParameters[0][1];
            return conversion_O, conversion_units_O;
        except SQLAlchemyError as e:
            print(e);
    # query data from data_stage01_isotopomer_mqresultstable
    def get_concAndConcUnits_sampleNameAndComponentName(self,sample_name_I,component_name_I):
        '''Querry data (i.e. concentration, area/peak height ratio) from sample name and component name
        NOTE: intended to be used within a for loop'''
        # check for absolute or relative quantitation (i.e. area/peak height ratio)
        try:
            use_conc = self.session.query(data_stage01_isotopomer_MQResultsTable.use_calculated_concentration).filter(
                    data_stage01_isotopomer_MQResultsTable.sample_name.like(sample_name_I),
                    data_stage01_isotopomer_MQResultsTable.component_name.like(component_name_I),
                    data_stage01_isotopomer_MQResultsTable.used_.is_(True)).all();
            if use_conc:
                use_conc_O = use_conc[0][0];
            else: 
                use_conc_O = None;
        except SQLAlchemyError as e:
            print(e);

        if use_conc_O:
            try:
                data = self.session.query(data_stage01_isotopomer_MQResultsTable.calculated_concentration,
                        data_stage01_isotopomer_MQResultsTable.conc_units).filter(
                        data_stage01_isotopomer_MQResultsTable.sample_name.like(sample_name_I),
                        data_stage01_isotopomer_MQResultsTable.component_name.like(component_name_I),
                        data_stage01_isotopomer_MQResultsTable.used_.is_(True)).all();
                if data:
                    conc_O = data[0][0];
                    conc_units_O = data[0][1];
                else: 
                    conc_O = None;
                    conc_units_O = None;
                return conc_O, conc_units_O;
            except SQLAlchemyError as e:
                print(e);

        else:
            # check for area or peak height ratio from quantitation_method
            try:
                data = self.session.query(quantitation_method.use_area).filter(
                        experiment.sample_name.like(sample_name_I),
                        experiment.quantitation_method_id.like(quantitation_method.id),
                        quantitation_method.component_name.like(component_name_I)).all();
                if data:
                    ratio_O = data[0][0];
                else: 
                    ratio_O = None;
            except SQLAlchemyError as e:
                print(e);

            if ratio_O:
                try:
                    data = self.session.query(data_stage01_isotopomer_MQResultsTable.area_ratio).filter(
                            data_stage01_isotopomer_MQResultsTable.sample_name.like(sample_name_I),
                            data_stage01_isotopomer_MQResultsTable.component_name.like(component_name_I),
                            data_stage01_isotopomer_MQResultsTable.used_.is_(True)).all();
                    if data:
                        conc_O = data[0][0];
                        conc_units_O = 'area_ratio';
                    else: 
                        conc_O = None;
                        conc_units_O = None;
                    return conc_O, conc_units_O;
                except SQLAlchemyError as e:
                    print(e);
            else:
                try:
                    data = self.session.query(data_stage01_isotopomer_MQResultsTable.height_ratio).filter(
                            data_stage01_isotopomer_MQResultsTable.sample_name.like(sample_name_I),
                            data_stage01_isotopomer_MQResultsTable.component_name.like(component_name_I),
                            data_stage01_isotopomer_MQResultsTable.used_.is_(True)).all();
                    if data:
                        conc_O = data[0][0];
                        conc_units_O = 'height_ratio';
                    else: 
                        conc_O = None;
                        conc_units_O = None;
                    return conc_O, conc_units_O;
                except SQLAlchemyError as e:
                    print(e);
    def get_peakHeight_sampleNameAndComponentName(self,sample_name_I,component_name_I):
        '''Querry peakHeight from sample name and component name
        NOTE: intended to be used within a for loop'''
        try:
            data = self.session.query(data_stage01_isotopomer_MQResultsTable.height).filter(
                    data_stage01_isotopomer_MQResultsTable.sample_name.like(sample_name_I),
                    data_stage01_isotopomer_MQResultsTable.component_name.like(component_name_I),
                    data_stage01_isotopomer_MQResultsTable.used_.is_(True)).all();
            if data:
                height_O = data[0][0];
            else: 
                height_O = None;
            return height_O
        except SQLAlchemyError as e:
            print(e);
    # query if used
    def get_used_sampleNameAndComponentName(self,sample_name_I,component_name_I):
        '''Querry used from sample name and component name
        NOTE: intended to be used within a for loop'''
        try:
            data = self.session.query(data_stage01_isotopomer_MQResultsTable.used_).filter(
                    data_stage01_isotopomer_MQResultsTable.sample_name.like(sample_name_I),
                    data_stage01_isotopomer_MQResultsTable.component_name_name.like(component_name_name_I)).all();
            if data:
                used_O = data[0];
            else: used_O = None;
            return used_O;
        except SQLAlchemyError as e:
            print(e);
    # delet data from data_stage01_isotopomer_mqresultstable
    def delete_row_sampleName(self,sampleNames_I):
        '''Delete specific samples from an experiment by their sample name'''
        deletes = [];
        for d in sampleNames_I:
            try:
                delete = self.session.query(data_stage01_isotopomer_MQResultsTable).filter(
                        data_stage01_isotopomer_MQResultsTable.sample_name.like(d['sample_name'])).delete(
                        synchronize_session=False);
                if delete == 0:
                    print('row not found')
                    print(d);
                deletes.append(delete);
            except SQLAlchemyError as e:
                print(e);
        self.session.commit();
        
    def add_dataStage01IsotopomerMQResultsTable(self,data_I):
        '''add rows of data_stage01_isotopomer_MQResultsTable'''
        if data_I:
            cnt = 0;
            for d in data_I:
                try:
                    if 'Index' in d:
                        data_add = data_stage01_isotopomer_MQResultsTable(d['Index'],
                            d['Sample Index'],
                            d['Original Filename'],
                            d['Sample Name'],
                            d['Sample ID'],
                            d['Sample Comment'],
                            d['Sample Type'],
                            d['Acquisition Date & Time'],
                            d['Rack Number'],
                            d['Plate Number'],
                            d['Vial Number'],
                            d['Dilution Factor'],
                            d['Injection Volume'],
                            d['Operator Name'],
                            d['Acq. Method Name'],
                            d['IS'],
                            d['Component Name'],
                            d['Component Index'],
                            d['Component Comment'],
                            d['IS Comment'],
                            d['Mass Info'],
                            d['IS Mass Info'],
                            d['IS Name'],
                            d['Component Group Name'],
                            d['Conc. Units'],
                            d['Failed Query'],
                            d['IS Failed Query'],
                            d['Peak Comment'],
                            d['IS Peak Comment'],
                            d['Actual Concentration'],
                            d['IS Actual Concentration'],
                            d['Concentration Ratio'],
                            d['Expected RT'],
                            d['IS Expected RT'],
                            d['Integration Type'],
                            d['IS Integration Type'],
                            d['Area'],
                            d['IS Area'],
                            d['Corrected Area'],
                            d['IS Corrected Area'],
                            d['Area Ratio'],
                            d['Height'],
                            d['IS Height'],
                            d['Corrected Height'],
                            d['IS Corrected Height'],
                            d['Height Ratio'],
                            d['Area / Height'],
                            d['IS Area / Height'],
                            d['Corrected Area/Height'],
                            d['IS Corrected Area/Height'],
                            d['Region Height'],
                            d['IS Region Height'],
                            d['Quality'],
                            d['IS Quality'],
                            d['Retention Time'],
                            d['IS Retention Time'],
                            d['Start Time'],
                            d['IS Start Time'],
                            d['End Time'],
                            d['IS End Time'],
                            d['Total Width'],
                            d['IS Total Width'],
                            d['Width at 50%'],
                            d['IS Width at 50%'],
                            d['Signal / Noise'],
                            d['IS Signal / Noise'],
                            d['Baseline Delta / Height'],
                            d['IS Baseline Delta / Height'],
                            d['Modified'],
                            d['Relative RT'],
                            d['Used'],
                            d['Calculated Concentration'],
                            d['Accuracy'],
                            d['Comment'],
                            d['Use_Calculated_Concentration']);
                    elif 'index_' in d:
                        data_add = data_stage01_isotopomer_MQResultsTable(d['index_'],
                            d['sample_index'],
                            d['original_filename'],
                            d['sample_name'],
                            d['sample_id'],
                            d['sample_comment'],
                            d['sample_type'],
                            d['acquisition_date_and_time'],
                            d['rack_number'],
                            d['plate_number'],
                            d['vial_number'],
                            d['dilution_factor'],
                            d['injection_volume'],
                            d['operator_name'],
                            d['acq_method_name'],
                            d['is_'],
                            d['component_name'],
                            d['component_index'],
                            d['component_comment'],
                            d['is_comment'],
                            d['mass_info'],
                            d['is_mass'],
                            d['is_name'],
                            d['component_group_name'],
                            d['conc_units'],
                            d['failed_query'],
                            d['is_failed_query'],
                            d['peak_comment'],
                            d['is_peak_comment'],
                            d['actual_concentration'],
                            d['is_actual_concentration'],
                            d['concentration_ratio'],
                            d['expected_rt'],
                            d['is_expected_rt'],
                            d['integration_type'],
                            d['is_integration_type'],
                            d['area'],
                            d['is_area'],
                            d['corrected_area'],
                            d['is_corrected_area'],
                            d['area_ratio'],
                            d['height'],
                            d['is_height'],
                            d['corrected_height'],
                            d['is_corrected_height'],
                            d['height_ratio'],
                            d['area_2_height'],
                            d['is_area_2_height'],
                            d['corrected_area2height'],
                            d['is_corrected_area2height'],
                            d['region_height'],
                            d['is_region_height'],
                            d['quality'],
                            d['is_quality'],
                            d['retention_time'],
                            d['is_retention_time'],
                            d['start_time'],
                            d['is_start_time'],
                            d['end_time'],
                            d['is_end_time'],
                            d['total_width'],
                            d['is_total_width'],
                            d['width_at_50'],
                            d['is_width_at_50'],
                            d['signal_2_noise'],
                            d['is_signal_2_noise'],
                            d['baseline_delta_2_height'],
                            d['is_baseline_delta_2_height'],
                            d['modified_'],
                            d['relative_rt'],
                            d['used_'],
                            d['calculated_concentration'],
                            d['accuracy_'],
                            d['comment_'],
                            d['use_calculated_concentration'],
                            );
                    self.session.add(data_add);
                    cnt = cnt + 1;
                    if cnt > 1000: 
                        self.session.commit();
                        cnt = 0;
                except IntegrityError as e:
                    print(e);
                except SQLAlchemyError as e:
                    print(e);
            self.session.commit();

    def update_dataStage01IsotopomerMQResultsTable(self,data_I):
        '''update rows of data_stage01_isotopomer_MQResultsTable'''
        if data_I:
            for d in data_I:
                try:
                    data_update = self.session.query(data_stage01_isotopomer_MQResultsTable).filter(
                            data_stage01_isotopomer_MQResultsTable.component_name.like(d['Component Name']),
                            data_stage01_isotopomer_MQResultsTable.sample_name.like(d['Sample Name']),
                            data_stage01_isotopomer_MQResultsTable.acquisition_date_and_time == d['Acquisition Date & Time']).update(
                            {'index_':d['Index'],
                            'sample_index':d['Sample Index'],
                            'original_filename':d['Original Filename'],
                            'sample_name':d['Sample Name'],
                            'sample_id':d['Sample ID'],
                            'sample_comment':d['Sample Comment'],
                            'sample_type':d['Sample Type'],
                            'acquisition_date_and_time':d['Acquisition Date & Time'],
                            'rack_number':d['Rack Number'],
                            'plate_number':d['Plate Number'],
                            'vial_number':d['Vial Number'],
                            'dilution_factor':d['Dilution Factor'],
                            'injection_volume':d['Injection Volume'],
                            'operator_name':d['Operator Name'],
                            'acq_method_name':d['Acq. Method Name'],
                            'is_':d['IS'],
                            'component_name':d['Component Name'],
                            'component_index':d['Component Index'],
                            'component_comment':d['Component Comment'],
                            'is_comment':d['IS Comment'],
                            'mass_info':d['Mass Info'],
                            'is_mass':d['IS Mass Info'],
                            'is_name':d['IS Name'],
                            'component_group_name':d['Component Group Name'],
                            'conc_units':d['Conc. Units'],
                            'failed_query':d['Failed Query'],
                            'is_failed_query':d['IS Failed Query'],
                            'peak_comment':d['Peak Comment'],
                            'is_peak_comment':d['IS Peak Comment'],
                            'actual_concentration':d['Actual Concentration'],
                            'is_actual_concentration':d['IS Actual Concentration'],
                            'concentration_ratio':d['Concentration Ratio'],
                            'expected_rt':d['Expected RT'],
                            'is_expected_rt':d['IS Expected RT'],
                            'integration_type':d['Integration Type'],
                            'is_integration_type':d['IS Integration Type'],
                            'area':d['Area'],
                            'is_area':d['IS Area'],
                            'corrected_area':d['Corrected Area'],
                            'is_corrected_area':d['IS Corrected Area'],
                            'area_ratio':d['Area Ratio'],
                            'height':d['Height'],
                            'is_height':d['IS Height'],
                            'corrected_height':d['Corrected Height'],
                            'is_corrected_height':d['IS Corrected Height'],
                            'height_ratio':d['Height Ratio'],
                            'area_2_height':d['Area / Height'],
                            'is_area_2_height':d['IS Area / Height'],
                            'corrected_area2height':d['Corrected Area/Height'],
                            'is_corrected_area2height':d['IS Corrected Area/Height'],
                            'region_height':d['Region Height'],
                            'is_region_height':d['IS Region Height'],
                            'quality':d['Quality'],
                            'is_quality':d['IS Quality'],
                            'retention_time':d['Retention Time'],
                            'is_retention_time':d['IS Retention Time'],
                            'start_time':d['Start Time'],
                            'is_start_time':d['IS Start Time'],
                            'end_time':d['End Time'],
                            'is_end_time':d['IS End Time'],
                            'total_width':d['Total Width'],
                            'is_total_width':d['IS Total Width'],
                            'width_at_50':d['Width at 50%'],
                            'is_width_at_50':d['IS Width at 50%'],
                            'signal_2_noise':d['Signal / Noise'],
                            'is_signal_2_noise':d['IS Signal / Noise'],
                            'baseline_delta_2_height':d['Baseline Delta / Height'],
                            'is_baseline_delta_2_height':d['IS Baseline Delta / Height'],
                            'modified_':d['Modified'],
                            'relative_rt':d['Relative RT'],
                            'used_':d['Used'],
                            'calculated_concentration':d['Calculated Concentration'],
                            'accuracy_':d['Accuracy'],
                            'comment_':d['Comment'],
                            'use_calculated_concentration':d['Use_Calculated_Concentration']},
                            synchronize_session=False);
                    if data_update == 0:
                        print('row not found.')
                        print(d);
                except SQLAlchemyError as e:
                    print(e);
            self.session.commit();