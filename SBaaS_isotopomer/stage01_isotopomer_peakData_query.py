from .stage01_isotopomer_peakData_postgresql_models import *
from SBaaS_LIMS.lims_experiment_postgresql_models import *
from SBaaS_LIMS.lims_sample_postgresql_models import *

from SBaaS_base.sbaas_base_query_update import sbaas_base_query_update
from SBaaS_base.sbaas_base_query_drop import sbaas_base_query_drop
from SBaaS_base.sbaas_base_query_initialize import sbaas_base_query_initialize
from SBaaS_base.sbaas_base_query_insert import sbaas_base_query_insert
from SBaaS_base.sbaas_base_query_select import sbaas_base_query_select
from SBaaS_base.sbaas_base_query_delete import sbaas_base_query_delete

from SBaaS_base.sbaas_template_query import sbaas_template_query

class stage01_isotopomer_peakData_query(sbaas_template_query):
    def initialize_supportedTables(self):
        '''Set the supported tables dict for 
        '''
        tables_supported = {'data_stage01_isotopomer_peakData':data_stage01_isotopomer_peakData,
            'data_stage01_isotopomer_peakList':data_stage01_isotopomer_peakList,
                        };
        self.set_supportedTables(tables_supported);
    def initialize_dataStage01_isotopomer_peakData(self):
        try:
            data_stage01_isotopomer_peakData.__table__.create(self.engine,True);
            data_stage01_isotopomer_peakList.__table__.create(self.engine,True);
        except SQLAlchemyError as e:
            print(e);
    def drop_dataStage01_isotopomer_peakData(self):
        try:
            data_stage01_isotopomer_peakData.__table__.drop(self.engine,True);
            data_stage01_isotopomer_peakList.__table__.drop(self.engine,True);
        except SQLAlchemyError as e:
            print(e);
    def reset_dataStage01_isotopomer_peakDataAndPeakList(self,experiment_id_I = None):
        try:
            if experiment_id_I:
                reset = self.session.query(data_stage01_isotopomer_peakData).filter(data_stage01_isotopomer_peakData.experiment_id.like(experiment_id_I)).delete(synchronize_session=False);
                reset = self.session.query(data_stage01_isotopomer_peakList).filter(data_stage01_isotopomer_peakList.experiment_id.like(experiment_id_I)).delete(synchronize_session=False);
                self.session.commit();
        except SQLAlchemyError as e:
            print(e);
    def reset_dataStage01_isotopomer_peakData(self,experiment_id_I):
        try:
            if experiment_id_I:
                reset = self.session.query(data_stage01_isotopomer_peakData).filter(data_stage01_isotopomer_peakData.experiment_id.like(experiment_id_I)).delete(synchronize_session=False);
                self.session.commit();
        except SQLAlchemyError as e:
            print(e);
    # query sample names from data_stage01_isotopomer_peakData
    def get_sampleNames_experimentIDAndSampleType_peakData(self,experiment_id_I,sample_type_I):
        '''Querry sample names (i.e. unknowns) that are used from
        the experiment'''
        try:
            sample_names = self.session.query(data_stage01_isotopomer_peakData.sample_name).filter(
                    data_stage01_isotopomer_peakData.experiment_id.like(experiment_id_I),
                    experiment.id.like(experiment_id_I),
                    experiment.sample_name.like(data_stage01_isotopomer_peakData.sample_name),
                    sample.sample_name.like( experiment.sample_name),
                    sample.sample_type.like(sample_type_I)).group_by(
                    data_stage01_isotopomer_peakData.sample_name).order_by(
                    data_stage01_isotopomer_peakData.sample_name.asc()).all();
            sample_names_O = [];
            for sn in sample_names: sample_names_O.append(sn.sample_name);
            return sample_names_O;
        except SQLAlchemyError as e:
            print(e);
    def get_sampleNames_experimentIDAndSampleTypeAndSampleNameAbbreviation_peakData(self,experiment_id_I,sample_type_I,sample_name_abbreviation_I):
        '''Querry sample names (i.e. unknowns) that are used from
        the experiment'''
        try:
            sample_names = self.session.query(data_stage01_isotopomer_peakData.sample_name).filter(
                    data_stage01_isotopomer_peakData.experiment_id.like(experiment_id_I),
                    experiment.id.like(experiment_id_I),
                    experiment.sample_name.like(data_stage01_isotopomer_peakData.sample_name),
                    sample.sample_name.like( experiment.sample_name),
                    sample.sample_type.like(sample_type_I),
                    sample_description.sample_id.like(sample.sample_id),
                    sample_description.sample_name_abbreviation.like(sample_name_abbreviation_I)).group_by(
                    data_stage01_isotopomer_peakData.sample_name).order_by(
                    data_stage01_isotopomer_peakData.sample_name.asc()).all();
            sample_names_O = [];
            for sn in sample_names: sample_names_O.append(sn.sample_name);
            return sample_names_O;
        except SQLAlchemyError as e:
            print(e);
    # query sample name abbreviations from data_stage01_isotopomer_peakData
    def get_sampleNameAbbreviationsAndOther_experimentIDAndSampleName_peakData(self,experiment_id_I,sample_name_I):
        '''Querry sample name abbreviations, time points and replicate numbers from
        the experiment by sample name'''
        try:
            sample_name_abbreviations = self.session.query(sample_description.sample_name_abbreviation,
                    sample_description.time_point,
                    sample_description.sample_replicate).filter(
                    data_stage01_isotopomer_peakData.sample_name.like(sample_name_I),
                    data_stage01_isotopomer_peakData.experiment_id.like(experiment_id_I),
                    data_stage01_isotopomer_peakData.sample_name.like(sample.sample_name),
                    sample.sample_id.like(sample_description.sample_id)).group_by(
                    sample_description.sample_name_abbreviation,
                    sample_description.time_point,
                    sample_description.sample_replicate).order_by(
                    sample_description.sample_name_abbreviation.asc()).all();
            sample_name_abbreviations_O = None;
            time_points_O = None;
            sample_replicates_O = None;
            if not sample_name_abbreviations: exit('bad query result: get_sampleNameAbbreviationsAndOther_experimentIDAndSampleName_peakData');
            sample_name_abbreviations_O=sample_name_abbreviations[0][0];
            time_points_O=sample_name_abbreviations[0][1];
            sample_replicates_O=sample_name_abbreviations[0][2];
            return sample_name_abbreviations_O,time_points_O,sample_replicates_O;
        except SQLAlchemyError as e:
            print(e);
    # query met_id, precursor formula from data_stage01_isotopomer_peakData
    def get_metIDAndPrecursorFormulaAndScanType_experimentIDAndSampleName_peakData(self,experiment_id_I,sample_name_I):
        '''Querry met_id, precursor formula that are used for the experiment'''
        try:
            component_names = self.session.query(data_stage01_isotopomer_peakData.met_id,
                    data_stage01_isotopomer_peakData.precursor_formula,
                    data_stage01_isotopomer_peakData.scan_type).filter(
                    data_stage01_isotopomer_peakData.sample_name.like(sample_name_I),
                    data_stage01_isotopomer_peakData.experiment_id.like(experiment_id_I)).group_by(
                    data_stage01_isotopomer_peakData.met_id,
                    data_stage01_isotopomer_peakData.precursor_formula,
                    data_stage01_isotopomer_peakData.scan_type).order_by(
                    data_stage01_isotopomer_peakData.met_id.asc(),
                    data_stage01_isotopomer_peakData.precursor_formula).all();
            met_ids_O = [];
            precursor_formulas_O = [];
            scan_type_O = [];
            if not component_names: exit('bad query result: get_metIDAndPrecursorFormula_experimentIDAndSampleName_peakData');
            for cn in component_names:
                met_ids_O.append(cn.met_id);
                precursor_formulas_O.append(cn.precursor_formula);
                scan_type_O.append(cn.scan_type);
            return met_ids_O, precursor_formulas_O, scan_type_O;
        except SQLAlchemyError as e:
            print(e);
    def get_scanType_experimentIDAndSampleName_peakData(self,experiment_id_I,sample_name_I):
        '''Querry scan type that are used for the experiment'''
        try:
            component_names = self.session.query(data_stage01_isotopomer_peakData.scan_type).filter(
                    data_stage01_isotopomer_peakData.sample_name.like(sample_name_I),
                    data_stage01_isotopomer_peakData.experiment_id.like(experiment_id_I)).group_by(
                    data_stage01_isotopomer_peakData.scan_type).order_by(
                    data_stage01_isotopomer_peakData.scan_type.asc()).all();
            scan_type_O = [];
            if not component_names: exit('bad query result: get_metIDAndPrecursorFormula_experimentIDAndSampleName_peakData');
            for cn in component_names:
                scan_type_O.append(cn[0]);
            return scan_type_O;
        except SQLAlchemyError as e:
            print(e);
    def get_metIDAndPrecursorFormula_experimentIDAndSampleNameAndScanType_peakData(self,experiment_id_I,sample_name_I,scan_type_I):
        '''Querry met_id, precursor formula that are used for the experiment'''
        try:
            component_names = self.session.query(data_stage01_isotopomer_peakData.met_id,
                    data_stage01_isotopomer_peakData.precursor_formula).filter(
                    data_stage01_isotopomer_peakData.sample_name.like(sample_name_I),
                    data_stage01_isotopomer_peakData.experiment_id.like(experiment_id_I),
                    data_stage01_isotopomer_peakData.scan_type.like(scan_type_I)).group_by(
                    data_stage01_isotopomer_peakData.met_id,
                    data_stage01_isotopomer_peakData.precursor_formula).order_by(
                    data_stage01_isotopomer_peakData.met_id.asc(),
                    data_stage01_isotopomer_peakData.precursor_formula).all();
            met_ids_O = [];
            precursor_formulas_O = [];
            if not component_names: exit('bad query result: get_metIDAndPrecursorFormula_experimentIDAndSampleNameAndScanType_peakData');
            for cn in component_names:
                met_ids_O.append(cn.met_id);
                precursor_formulas_O.append(cn.precursor_formula);
            return met_ids_O, precursor_formulas_O;
        except SQLAlchemyError as e:
            print(e);
    def get_metIDAndPrecursorFormula_experimentIDAndSampleNameAndScanTypeAndMetID_peakData(self,experiment_id_I,sample_name_I,scan_type_I,met_id_I):
        '''Querry met_id, precursor formula that are used for the experiment'''
        try:
            component_names = self.session.query(data_stage01_isotopomer_peakData.met_id,
                    data_stage01_isotopomer_peakData.precursor_formula).filter(
                    data_stage01_isotopomer_peakData.sample_name.like(sample_name_I),
                    data_stage01_isotopomer_peakData.met_id.like(met_id_I),
                    data_stage01_isotopomer_peakData.experiment_id.like(experiment_id_I),
                    data_stage01_isotopomer_peakData.scan_type.like(scan_type_I)).group_by(
                    data_stage01_isotopomer_peakData.met_id,
                    data_stage01_isotopomer_peakData.precursor_formula).order_by(
                    data_stage01_isotopomer_peakData.met_id.asc(),
                    data_stage01_isotopomer_peakData.precursor_formula).all();
            met_ids_O = [];
            precursor_formulas_O = [];
            if not component_names: exit('bad query result: get_metIDAndPrecursorFormula_experimentIDAndSampleNameAndScanType_peakData');
            for cn in component_names:
                met_ids_O.append(cn.met_id);
                precursor_formulas_O.append(cn.precursor_formula);
            return met_ids_O, precursor_formulas_O;
        except SQLAlchemyError as e:
            print(e);
    # query data from data_stage01_isotopomer_peakData
    def get_data_experimentIDAndSampleNameAndMetIDAndPrecursorFormulaAndScanType_peakData(self,experiment_id_I,sample_name_I,met_id_I,precursor_formula_I,scan_type_I):
        '''Querry peak data for a specific experiment_id, sample_name, met_id, and precursor_formula'''
        try:
            data = self.session.query(data_stage01_isotopomer_peakData.mass,
                    data_stage01_isotopomer_peakData.mass_units,
                    data_stage01_isotopomer_peakData.intensity,
                    data_stage01_isotopomer_peakData.intensity_units).filter(
                    data_stage01_isotopomer_peakData.sample_name.like(sample_name_I),
                    data_stage01_isotopomer_peakData.experiment_id.like(experiment_id_I),
                    data_stage01_isotopomer_peakData.met_id.like(met_id_I),
                    data_stage01_isotopomer_peakData.precursor_formula.like(precursor_formula_I),
                    data_stage01_isotopomer_peakData.scan_type.like(scan_type_I)).order_by(
                    data_stage01_isotopomer_peakData.mass.asc()).all();
            data_O = {};
            if not data: exit('bad query result: get_data_experimentIDAndSampleNameAndMetIDAndPrecursorFormula_peakData');
            for d in data:
                data_O[d.mass] = d.intensity;
            return data_O;
        except SQLAlchemyError as e:
            print(e);

    def add_peakData(self, data_I, experiment_id, samplename, precursor_formula, met_id,
                          mass_units_I,intensity_units_I, scan_type_I):
        '''add rows of data_stage01_isotopomer_peakData'''
        if data_I:
            for d in data_I:
                try:
                    data_add = data_stage01_isotopomer_peakData(experiment_id,
                            samplename,
                            met_id,
                            precursor_formula,
                            d['Mass/Charge'],
                            #d['mass'],
                            mass_units_I,
                            d['Intensity'],
                            #d['intensity'],
                            intensity_units_I,
                            scan_type_I,
                            True);
                    self.session.add(data_add);
                except SQLAlchemyError as e:
                    print(e);
            self.session.commit();

    def add_peakList(self, data_I, experiment_id, samplename, precursor_formula, met_id,
                            mass_units_I='Da',intensity_units_I='cps',
                            centroid_mass_units_I='Da', peak_start_units_I='Da',
                            peak_stop_units_I='Da', resolution_I=None, scan_type_I='EPI'):
        '''add rows of data_stage01_isotopomer_peakList'''
        if data_I:
            for d in data_I:
                try:
                    data_add = data_stage01_isotopomer_peakList(experiment_id,
                            samplename,
                            met_id,
                            precursor_formula,
                            d['mass'],
                            mass_units_I,
                            d['intensity'],
                            intensity_units_I,
                            d['centroid_mass'],
                            centroid_mass_units_I,
                            d['peak_start'],
                            peak_start_units_I,
                            d['peak_stop'],
                            peak_stop_units_I,
                            resolution_I,
                            scan_type_I);
                    self.session.add(data_add);
                except SQLAlchemyError as e:
                    print(e);
            self.session.commit();