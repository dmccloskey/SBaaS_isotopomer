#LIMS
from SBaaS_LIMS.lims_msMethod_postgresql_models import *
#SBaaS
from .stage01_isotopomer_averages_postgresql_models import *

from SBaaS_base.sbaas_base_query_update import sbaas_base_query_update
from SBaaS_base.sbaas_base_query_drop import sbaas_base_query_drop
from SBaaS_base.sbaas_base_query_initialize import sbaas_base_query_initialize
from SBaaS_base.sbaas_base_query_insert import sbaas_base_query_insert
from SBaaS_base.sbaas_base_query_select import sbaas_base_query_select
from SBaaS_base.sbaas_base_query_delete import sbaas_base_query_delete

from SBaaS_base.sbaas_template_query import sbaas_template_query

class stage01_isotopomer_averages_query(sbaas_template_query):
    def initialize_supportedTables(self):
        '''Set the supported tables dict for 
        '''
        tables_supported = {'data_stage01_isotopomer_averages':data_stage01_isotopomer_averages,
                'data_stage01_isotopomer_averagesNormSum':data_stage01_isotopomer_averagesNormSum,
                        };
        self.set_supportedTables(tables_supported);
    def initialize_dataStage01_isotopomer_averages(self):
        try:
            data_stage01_isotopomer_averages.__table__.create(self.engine,True);
            data_stage01_isotopomer_averagesNormSum.__table__.create(self.engine,True);
        except SQLAlchemyError as e:
            print(e);
    def drop_dataStage01_isotopomer_averages(self):
        try:
            data_stage01_isotopomer_averages.__table__.drop(self.engine,True);
            data_stage01_isotopomer_averagesNormSum.__table__.drop(self.engine,True);
        except SQLAlchemyError as e:
            print(e);
    def reset_dataStage01_isotopomer_averages(self,experiment_id_I,sample_name_abbreviations_I=[],scan_types_I=[]):
        try:
            if experiment_id_I and sample_name_abbreviations_I and scan_types_I:
                for sna in sample_name_abbreviations_I:
                    for st in scan_types_I:
                        reset = self.session.query(data_stage01_isotopomer_averages).filter(
                            data_stage01_isotopomer_averages.experiment_id.like(experiment_id_I),
                            data_stage01_isotopomer_averages.sample_name_abbreviation.like(sna),
                            data_stage01_isotopomer_averages.scan_type.like(st)).delete(synchronize_session=False);
                        reset = self.session.query(data_stage01_isotopomer_averagesNormSum).filter(
                            data_stage01_isotopomer_averagesNormSum.experiment_id.like(experiment_id_I),
                            data_stage01_isotopomer_averagesNormSum.sample_name_abbreviation.like(sna),
                            data_stage01_isotopomer_averagesNormSum.scan_type.like(st)).delete(synchronize_session=False);
                self.session.commit();
            if experiment_id_I and sample_name_abbreviations_I:
                for sna in sample_name_abbreviations_I:
                    reset = self.session.query(data_stage01_isotopomer_averages).filter(
                        data_stage01_isotopomer_averages.experiment_id.like(experiment_id_I),
                        data_stage01_isotopomer_averages.sample_name_abbreviation.like(sna)).delete(synchronize_session=False);
                    reset = self.session.query(data_stage01_isotopomer_averagesNormSum).filter(
                        data_stage01_isotopomer_averagesNormSum.experiment_id.like(experiment_id_I),
                        data_stage01_isotopomer_averagesNormSum.sample_name_abbreviation.like(sna)).delete(synchronize_session=False);
                self.session.commit();
            elif experiment_id_I:
                reset = self.session.query(data_stage01_isotopomer_averages).filter(data_stage01_isotopomer_averages.experiment_id.like(experiment_id_I)).delete(synchronize_session=False);
                reset = self.session.query(data_stage01_isotopomer_averagesNormSum).filter(data_stage01_isotopomer_averagesNormSum.experiment_id.like(experiment_id_I)).delete(synchronize_session=False);
                self.session.commit();
        except SQLAlchemyError as e:
            print(e);
    ## Query data from data_stage01_isotopomer_averages:
    # query normalized intensity from data_stage01_isotopomer_averages
    def get_normalizedIntensity_experimentIDAndSampleAbbreviationAndTimePointAndMetIDAndFragmentFormulaAndMassAndScanType_dataStage01Averages(self,experiment_id_I,sample_name_abbreviation_I,time_point_I,met_id_I,fragment_formula_I,fragment_mass_I,scan_type_I):
        '''Querry peak data for a specific experiment_id, sample_name, met_id, and scan type'''
        try:
            data = self.session.query(data_stage01_isotopomer_averages.intensity_normalized_average,
                    data_stage01_isotopomer_averages.intensity_normalized_cv,
                    data_stage01_isotopomer_averages.intensity_normalized_units).filter(
                    data_stage01_isotopomer_averages.sample_name_abbreviation.like(sample_name_abbreviation_I),
                    data_stage01_isotopomer_averages.time_point.like(time_point_I),
                    data_stage01_isotopomer_averages.fragment_formula.like(fragment_formula_I),
                    data_stage01_isotopomer_averages.fragment_mass == fragment_mass_I,
                    data_stage01_isotopomer_averages.experiment_id.like(experiment_id_I),
                    data_stage01_isotopomer_averages.met_id.like(met_id_I),
                    data_stage01_isotopomer_averages.scan_type.like(scan_type_I),
                    data_stage01_isotopomer_averages.used_).all();
            intensity_normalized_average_O = None;
            intensity_normalized_cv_O = None;
            intensity_normalized_units_O = None;
            if not data:
                print('No normalized intensities found for the following:')
                print('sample_name_abbreviation\ttime_point\tmet_id\tfragment_formula\tfragment_mass\tscan_type');
                print((sample_name_abbreviation_I) + '\t' + str(time_point_I) + '\t' + str(met_id_I) + '\t' + str(fragment_formula_I) + '\t' + str(fragment_mass_I) + '\t' + str(scan_type_I));
                return intensity_normalized_average_O,intensity_normalized_cv_O;
            else:
                intensity_normalized_average_O = data[0][0];
                intensity_normalized_cv_O = data[0][1];
                intensity_normalized_units_O = data[0][2];
                return intensity_normalized_average_O,intensity_normalized_cv_O;
        except SQLAlchemyError as e:
            print(e);
    # query time points from data_stage01_isotopomer_averages:
    def get_timePoint_experimentID_dataStage01Averages(self,experiment_id_I):
        '''Querry time points that are used from the experiment and sample name'''
        try:
            time_points = self.session.query(data_stage01_isotopomer_averages.time_point).filter(
                    data_stage01_isotopomer_averages.experiment_id.like(experiment_id_I),
                    data_stage01_isotopomer_averages.used_.is_(True)).group_by(
                    data_stage01_isotopomer_averages.time_point).order_by(
                    data_stage01_isotopomer_averages.time_point.asc()).all();
            time_points_O = [];
            for tp in time_points: time_points_O.append(tp.time_point);
            return time_points_O;
        except SQLAlchemyError as e:
            print(e);
    # query sample name abbreviations from data_stage01_isotopomer_averages:
    def get_sampleNameAbbreviations_experimentIDAndSampleTypeAndTimePoint_dataStage01Averages(self,experiment_id_I,sample_type_I,time_point_I):
        '''Querry sample name abbreviations that are used from
        the experiment for specific time-points'''
        try:
            sample_name_abbreviations = self.session.query(
                    data_stage01_isotopomer_averages.sample_name_abbreviation).filter(
                    data_stage01_isotopomer_averages.experiment_id.like(experiment_id_I),
                    data_stage01_isotopomer_averages.used_.is_(True),
                    data_stage01_isotopomer_averages.sample_type.like(sample_type_I),
                    data_stage01_isotopomer_averages.time_point.like(time_point_I)).group_by(
                    data_stage01_isotopomer_averages.sample_name_abbreviation).order_by(
                    data_stage01_isotopomer_averages.sample_name_abbreviation).all();
            sample_name_abbreviations_O = [];
            for sn in sample_name_abbreviations:
                sample_name_abbreviations_O.append(sn[0]);
            return sample_name_abbreviations_O;
        except SQLAlchemyError as e:
            print(e);
    # query scan types from data_stage01_isotopomer_averages
    def get_scanTypes_experimentIDAndTimePointAndSampleAbbreviationsAndSampleType_dataStage01Averages(self,experiment_id_I,time_point_I,sample_name_abbreviations_I,sample_type_I):
        '''Querry scan types that are used from the experiment for specific time-points and sample name abbreviations'''
        try:
            scan_types = self.session.query(
                    data_stage01_isotopomer_averages.scan_type).filter(
                    data_stage01_isotopomer_averages.experiment_id.like(experiment_id_I),
                    data_stage01_isotopomer_averages.used_.is_(True),
                    data_stage01_isotopomer_averages.time_point.like(time_point_I),
                    data_stage01_isotopomer_averages.sample_type.like(sample_type_I),
                    data_stage01_isotopomer_averages.sample_name_abbreviation.like(sample_name_abbreviations_I)).group_by(
                    data_stage01_isotopomer_averages.scan_type).order_by(
                    data_stage01_isotopomer_averages.scan_type).all();
            scan_types_O = [];
            for st in scan_types:
                scan_types_O.append(st[0]);
            return scan_types_O;
        except SQLAlchemyError as e:
            print(e);
    # query met_ids  from data_stage01_isotopomer_averages
    def get_metIDs_experimentIDAndSampleAbbreviationAndTimePointAndSampleTypeAndScanType_dataStage01Averages(self,experiment_id_I,sample_name_abbreviation_I,time_point_I,sample_type_I,scan_type_I):
        '''Querry met ids that are used for the experiment, sample abbreviation, time point, scan type'''
        try:
            met_ids = self.session.query(data_stage01_isotopomer_averages.met_id).filter(
                    data_stage01_isotopomer_averages.sample_name_abbreviation.like(sample_name_abbreviation_I),
                    data_stage01_isotopomer_averages.experiment_id.like(experiment_id_I),
                    data_stage01_isotopomer_averages.time_point.like(time_point_I),
                    data_stage01_isotopomer_averages.sample_type.like(sample_type_I),
                    data_stage01_isotopomer_averages.scan_type.like(scan_type_I),
                    data_stage01_isotopomer_averages.used_.is_(True)).group_by(
                    data_stage01_isotopomer_averages.met_id).order_by(
                    data_stage01_isotopomer_averages.met_id.asc()).all();
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
    # query normalized intensity from data_stage01_isotopomer_averages
    def get_dataProductFragment_experimentIDAndTimePointSampleAbbreviationAndSampleTypeAndScanTypeAndMetID_dataStage01Averages(self,experiment_id_I,sample_name_abbreviation_I,time_point_I,sample_type_I,scan_type_I, met_id_I):
        '''Querry peak data for a specific experiment_id, sample_name_abbreviation'''
        try:
            data = self.session.query(data_stage01_isotopomer_averages.fragment_formula,
                    data_stage01_isotopomer_averages.fragment_mass,
                    MS_components.product_fragment,
                    data_stage01_isotopomer_averages.intensity_normalized_average,
                    data_stage01_isotopomer_averages.intensity_normalized_cv,
                    data_stage01_isotopomer_averages.intensity_theoretical,
                    data_stage01_isotopomer_averages.abs_devFromTheoretical,
                    data_stage01_isotopomer_spectrumAccuracy.spectrum_accuracy,
                    data_stage01_isotopomer_averages.scan_type).filter(
                    data_stage01_isotopomer_averages.sample_name_abbreviation.like(sample_name_abbreviation_I),
                    data_stage01_isotopomer_averages.experiment_id.like(experiment_id_I),
                    data_stage01_isotopomer_averages.time_point.like(time_point_I),
                    data_stage01_isotopomer_averages.sample_type.like(sample_type_I),
                    data_stage01_isotopomer_averages.scan_type.like(scan_type_I),
                    data_stage01_isotopomer_averages.met_id.like(met_id_I),
                    data_stage01_isotopomer_averages.fragment_formula.like(MS_components.product_formula),
                    data_stage01_isotopomer_averages.met_id.like(MS_components.met_id),
                    MS_components.ms_methodtype.like('tuning'),
                    data_stage01_isotopomer_averages.used_,
                    data_stage01_isotopomer_spectrumAccuracy.sample_name_abbreviation.like(sample_name_abbreviation_I),
                    data_stage01_isotopomer_spectrumAccuracy.experiment_id.like(experiment_id_I),
                    data_stage01_isotopomer_spectrumAccuracy.time_point.like(time_point_I),
                    data_stage01_isotopomer_spectrumAccuracy.sample_type.like(sample_type_I),
                    data_stage01_isotopomer_spectrumAccuracy.scan_type.like(scan_type_I),
                    data_stage01_isotopomer_spectrumAccuracy.met_id.like(met_id_I),
                    data_stage01_isotopomer_spectrumAccuracy.used_.is_(True),
                    data_stage01_isotopomer_spectrumAccuracy.fragment_formula.like(MS_components.product_formula),
                    data_stage01_isotopomer_spectrumAccuracy.met_id.like(MS_components.met_id)).group_by(
                    data_stage01_isotopomer_averages.fragment_formula,
                    data_stage01_isotopomer_averages.fragment_mass,
                    MS_components.product_fragment,
                    data_stage01_isotopomer_averages.intensity_normalized_average,
                    data_stage01_isotopomer_averages.intensity_normalized_cv,
                    data_stage01_isotopomer_averages.intensity_theoretical,
                    data_stage01_isotopomer_averages.abs_devFromTheoretical,
                    data_stage01_isotopomer_spectrumAccuracy.spectrum_accuracy,
                    data_stage01_isotopomer_averages.scan_type).order_by(
                    data_stage01_isotopomer_averages.fragment_formula.desc(),
                    data_stage01_isotopomer_averages.fragment_mass.asc()).all();
            data_O = [];
            if not data:
                print('No normalized intensities found for the following:')
                print('sample_name_abbreviation: ' + sample_name_abbreviation_I);
                return data_O;
            else:
                # algorithm will break there is no data for a0 mass and there are jumps in the a values (i.e. a0 to a2);
                fragment_formula = '';
                fragment_formula_old = '';
                data_cnt = len(data)-1;
                i = 0;
                while i <= data_cnt:
                    fragment_formula_old = data[i].fragment_formula;
                    row_key = [];
                    row_theoretical = [];
                    row_measured = [];
                    row_measured_cv = [];
                    row_measured_dif = [];
                    row_spectrum_accuracy = [];
                    row = [];
                    for a in range(50):
                        if i <= data_cnt:
                            fragment_formula = data[i].fragment_formula;
                            if fragment_formula == fragment_formula_old:
                                if a == 0:
                                    # add key columns
                                    row_key.append(sample_name_abbreviation_I);
                                    row_key.append(time_point_I);
                                    row_key.append(met_id_I);
                                    row_key.append(data[i].fragment_formula);
                                    row_key.append(str(data[i].product_fragment));
                                    row_key.append(data[i].scan_type);
                                    row_spectrum_accuracy.append(data[i].spectrum_accuracy);
                                    mass0 = data[i].fragment_mass
                                massi = data[i].fragment_mass;
                                massDif = massi-mass0;
                                # add a+0... information
                                if data[i].intensity_theoretical: theoretical = numpy.round(data[i].intensity_theoretical,3);
                                else: theoretical = data[i].intensity_theoretical;
                                row_theoretical.append(theoretical)
                                if data[i].intensity_normalized_average: measured = numpy.round(data[i].intensity_normalized_average,3);
                                else: measured = data[i].intensity_normalized_average;
                                row_measured.append(measured)
                                if data[i].intensity_normalized_cv: cv = numpy.round(data[i].intensity_normalized_cv,3);
                                else: cv = data[i].intensity_normalized_cv;
                                row_measured_cv.append(cv);
                                if data[i].abs_devFromTheoretical: dif = numpy.round(data[i].abs_devFromTheoretical,3)
                                else: dif = data[i].abs_devFromTheoretical;
                                row_measured_dif.append(dif)
                                i += 1;
                            else:
                                row_theoretical.append(None);
                                row_measured.append(None);
                                row_measured_cv.append(None);
                                row_measured_dif.append(None);
                        else:
                            row_theoretical.append(None);
                            row_measured.append(None);
                            row_measured_cv.append(None);
                            row_measured_dif.append(None);
                    row.extend(row_key);
                    row.extend(row_theoretical);
                    row.extend(row_measured);
                    row.extend(row_measured_cv);
                    row.extend(row_measured_dif);
                    row.extend(row_spectrum_accuracy);
                    data_O.append(row);
                return data_O;
        except SQLAlchemyError as e:
            print(e);
    def get_dataPrecursorFragment_experimentIDAndTimePointSampleAbbreviationAndSampleTypeAndScanTypeAndMetID_dataStage01Averages(self,experiment_id_I,sample_name_abbreviation_I,time_point_I,sample_type_I,scan_type_I, met_id_I):
        '''Querry peak data for a specific experiment_id, sample_name_abbreviation'''
        try:
            data = self.session.query(data_stage01_isotopomer_averages.fragment_formula,
                    data_stage01_isotopomer_averages.fragment_mass,
                    MS_components.precursor_fragment,
                    data_stage01_isotopomer_averages.intensity_normalized_average,
                    data_stage01_isotopomer_averages.intensity_normalized_cv,
                    data_stage01_isotopomer_averages.intensity_theoretical,
                    data_stage01_isotopomer_averages.abs_devFromTheoretical,
                    data_stage01_isotopomer_spectrumAccuracy.spectrum_accuracy,
                    data_stage01_isotopomer_averages.scan_type).filter(
                    data_stage01_isotopomer_averages.sample_name_abbreviation.like(sample_name_abbreviation_I),
                    data_stage01_isotopomer_averages.experiment_id.like(experiment_id_I),
                    data_stage01_isotopomer_averages.time_point.like(time_point_I),
                    data_stage01_isotopomer_averages.sample_type.like(sample_type_I),
                    data_stage01_isotopomer_averages.scan_type.like(scan_type_I),
                    data_stage01_isotopomer_averages.met_id.like(met_id_I),
                    data_stage01_isotopomer_averages.fragment_formula.like(MS_components.precursor_formula),
                    data_stage01_isotopomer_averages.met_id.like(MS_components.met_id),
                    MS_components.ms_methodtype.like('tuning'),
                    data_stage01_isotopomer_averages.used_,
                    data_stage01_isotopomer_spectrumAccuracy.sample_name_abbreviation.like(sample_name_abbreviation_I),
                    data_stage01_isotopomer_spectrumAccuracy.experiment_id.like(experiment_id_I),
                    data_stage01_isotopomer_spectrumAccuracy.time_point.like(time_point_I),
                    data_stage01_isotopomer_spectrumAccuracy.sample_type.like(sample_type_I),
                    data_stage01_isotopomer_spectrumAccuracy.scan_type.like(scan_type_I),
                    data_stage01_isotopomer_spectrumAccuracy.met_id.like(met_id_I),
                    data_stage01_isotopomer_spectrumAccuracy.used_.is_(True),
                    data_stage01_isotopomer_spectrumAccuracy.fragment_formula.like(MS_components.precursor_formula),
                    data_stage01_isotopomer_spectrumAccuracy.met_id.like(MS_components.met_id)).group_by(
                    data_stage01_isotopomer_averages.fragment_formula,
                    data_stage01_isotopomer_averages.fragment_mass,
                    MS_components.precursor_fragment,
                    data_stage01_isotopomer_averages.intensity_normalized_average,
                    data_stage01_isotopomer_averages.intensity_normalized_cv,
                    data_stage01_isotopomer_averages.intensity_theoretical,
                    data_stage01_isotopomer_averages.abs_devFromTheoretical,
                    data_stage01_isotopomer_spectrumAccuracy.spectrum_accuracy,
                    data_stage01_isotopomer_averages.scan_type).order_by(
                    data_stage01_isotopomer_averages.fragment_formula.desc(),
                    data_stage01_isotopomer_averages.fragment_mass.asc()).all();
            data_O = [];
            if not data:
                print('No normalized intensities found for the following:')
                print('sample_name_abbreviation: ' + sample_name_abbreviation_I);
                return data_O;
            else:
                # algorithm will break there is no data for a0 mass and there are jumps in the a values (i.e. a0 to a2);
                fragment_formula = '';
                fragment_formula_old = '';
                data_cnt = len(data)-1;
                i = 0;
                while i <= data_cnt:
                    fragment_formula_old = data[i].fragment_formula;
                    row_key = [];
                    row_theoretical = [];
                    row_measured = [];
                    row_measured_cv = [];
                    row_measured_dif = [];
                    row_spectrum_accuracy = [];
                    row = [];
                    for a in range(50):
                        if i <= data_cnt:
                            fragment_formula = data[i].fragment_formula;
                            if fragment_formula == fragment_formula_old:
                                if a == 0:
                                    # add key columns
                                    row_key.append(sample_name_abbreviation_I);
                                    row_key.append(time_point_I);
                                    row_key.append(met_id_I);
                                    row_key.append(data[i].fragment_formula);
                                    row_key.append(str(data[i].precursor_fragment));
                                    row_key.append(data[i].scan_type);
                                    row_spectrum_accuracy.append(data[i].spectrum_accuracy);
                                    mass0 = data[i].fragment_mass
                                massi = data[i].fragment_mass;
                                massDif = massi-mass0;
                                # add a+0... information
                                if data[i].intensity_theoretical: theoretical = numpy.round(data[i].intensity_theoretical,3);
                                else: theoretical = data[i].intensity_theoretical;
                                row_theoretical.append(theoretical)
                                if data[i].intensity_normalized_average: measured = numpy.round(data[i].intensity_normalized_average,3);
                                else: measured = data[i].intensity_normalized_average;
                                row_measured.append(measured)
                                if data[i].intensity_normalized_cv: cv = numpy.round(data[i].intensity_normalized_cv,3);
                                else: cv = data[i].intensity_normalized_cv;
                                row_measured_cv.append(cv);
                                if data[i].abs_devFromTheoretical: dif = numpy.round(data[i].abs_devFromTheoretical,3)
                                else: dif = data[i].abs_devFromTheoretical;
                                row_measured_dif.append(dif)
                                i += 1;
                            else:
                                row_theoretical.append(None);
                                row_measured.append(None);
                                row_measured_cv.append(None);
                                row_measured_dif.append(None);
                        else:
                            row_theoretical.append(None);
                            row_measured.append(None);
                            row_measured_cv.append(None);
                            row_measured_dif.append(None);
                    row.extend(row_key);
                    row.extend(row_theoretical);
                    row.extend(row_measured);
                    row.extend(row_measured_cv);
                    row.extend(row_measured_dif);
                    row.extend(row_spectrum_accuracy);
                    data_O.append(row);
                return data_O;
        except SQLAlchemyError as e:
            print(e);
    # query used and comment from data_stage01_isotopomer_averages
    def get_row_experimentID_dataStage01Averages(self,experiment_id_I):
        '''Querry row information (used and comment) from data_stage01_isotopomer_averages'''
        try:
            data = self.session.query(data_stage01_isotopomer_averages.experiment_id,
                    data_stage01_isotopomer_averages.sample_name_abbreviation,
                    data_stage01_isotopomer_averages.sample_type,
                    data_stage01_isotopomer_averages.time_point,
                    data_stage01_isotopomer_averages.met_id,
                    data_stage01_isotopomer_averages.fragment_formula,
                    data_stage01_isotopomer_averages.fragment_mass,
                    data_stage01_isotopomer_averages.scan_type,
                    data_stage01_isotopomer_averages.used_,
                    data_stage01_isotopomer_averages.comment_).filter(
                    data_stage01_isotopomer_averages.experiment_id.like(experiment_id_I)).all();
            data_O = [];
            if not data:
                print(('No row information found for experiment_id: ' + experiment_id_I));
                return data_O;
            else:
                for d in data:
                    data_tmp = {};
                    data_tmp['experiment_id']=d.experiment_id;
                    data_tmp['sample_name_abbreviation']=d.sample_name_abbreviation;
                    data_tmp['sample_type']=d.sample_type;
                    data_tmp['time_point']=d.time_point;
                    data_tmp['met_id']=d.met_id;
                    data_tmp['fragment_formula']=d.fragment_formula;
                    data_tmp['fragment_mass']=d.fragment_mass;
                    data_tmp['scan_type']=d.scan_type;
                    data_tmp['used_']=d.used_;
                    data_tmp['comment_']=d.comment_;
                    data_O.append(data_tmp);
                return data_O;
        except SQLAlchemyError as e:
            print(e);
    ## Query from data_stage01_isotopomer_averagesNormSum:
    # query time points from data_stage01_isotopomer_averagesNormSum:
    def get_timePoint_experimentID_dataStage01AveragesNormSum(self,experiment_id_I):
        '''Querry time points that are used from the experiment'''
        try:
            time_points = self.session.query(data_stage01_isotopomer_averagesNormSum.time_point).filter(
                    data_stage01_isotopomer_averagesNormSum.experiment_id.like(experiment_id_I),
                    data_stage01_isotopomer_averagesNormSum.used_.is_(True)).group_by(
                    data_stage01_isotopomer_averagesNormSum.time_point).order_by(
                    data_stage01_isotopomer_averagesNormSum.time_point.asc()).all();
            time_points_O = [];
            for tp in time_points: time_points_O.append(tp.time_point);
            return time_points_O;
        except SQLAlchemyError as e:
            print(e);
    def get_timePoint_experimentIDAndSampleNameAbbreviation_dataStage01AveragesNormSum(self,experiment_id_I,sample_name_abbreviation_I):
        '''Querry time points that are used from the experiment and sample name abbreviation'''
        try:
            time_points = self.session.query(data_stage01_isotopomer_averagesNormSum.time_point).filter(
                    data_stage01_isotopomer_averagesNormSum.experiment_id.like(experiment_id_I),
                    data_stage01_isotopomer_averagesNormSum.sample_name_abbreviation.like(sample_name_abbreviation_I),
                    data_stage01_isotopomer_averagesNormSum.used_.is_(True)).group_by(
                    data_stage01_isotopomer_averagesNormSum.time_point).order_by(
                    data_stage01_isotopomer_averagesNormSum.time_point.asc()).all();
            time_points_O = [];
            for tp in time_points: time_points_O.append(tp.time_point);
            return time_points_O;
        except SQLAlchemyError as e:
            print(e);
    # query sample name abbreviations from data_stage01_isotopomer_averagesNormSum:
    def get_sampleNameAbbreviations_experimentIDAndSampleType_dataStage01AveragesNormSum(self,experiment_id_I,sample_type_I):
        '''Querry sample name abbreviations that are used from
        the experiment'''
        try:
            sample_name_abbreviations = self.session.query(
                    data_stage01_isotopomer_averagesNormSum.sample_name_abbreviation).filter(
                    data_stage01_isotopomer_averagesNormSum.experiment_id.like(experiment_id_I),
                    data_stage01_isotopomer_averagesNormSum.used_.is_(True),
                    data_stage01_isotopomer_averagesNormSum.sample_type.like(sample_type_I)).group_by(
                    data_stage01_isotopomer_averagesNormSum.sample_name_abbreviation).order_by(
                    data_stage01_isotopomer_averagesNormSum.sample_name_abbreviation).all();
            sample_name_abbreviations_O = [];
            for sn in sample_name_abbreviations:
                sample_name_abbreviations_O.append(sn[0]);
            return sample_name_abbreviations_O;
        except SQLAlchemyError as e:
            print(e);
    def get_sampleNameAbbreviations_experimentIDAndSampleTypeAndTimePoint_dataStage01AveragesNormSum(self,experiment_id_I,sample_type_I,time_point_I):
        '''Querry sample name abbreviations that are used from
        the experiment for specific time-points'''
        try:
            sample_name_abbreviations = self.session.query(
                    data_stage01_isotopomer_averagesNormSum.sample_name_abbreviation).filter(
                    data_stage01_isotopomer_averagesNormSum.experiment_id.like(experiment_id_I),
                    data_stage01_isotopomer_averagesNormSum.used_.is_(True),
                    data_stage01_isotopomer_averagesNormSum.sample_type.like(sample_type_I),
                    data_stage01_isotopomer_averagesNormSum.time_point.like(time_point_I)).group_by(
                    data_stage01_isotopomer_averagesNormSum.sample_name_abbreviation).order_by(
                    data_stage01_isotopomer_averagesNormSum.sample_name_abbreviation).all();
            sample_name_abbreviations_O = [];
            for sn in sample_name_abbreviations:
                sample_name_abbreviations_O.append(sn[0]);
            return sample_name_abbreviations_O;
        except SQLAlchemyError as e:
            print(e);
    # query scan types from data_stage01_isotopomer_averagesNormSum
    def get_scanTypes_experimentIDAndTimePointAndSampleAbbreviationsAndSampleType_dataStage01AveragesNormSum(self,experiment_id_I,time_point_I,sample_name_abbreviations_I,sample_type_I):
        '''Querry scan types that are used from the experiment for specific time-points and sample name abbreviations'''
        try:
            scan_types = self.session.query(
                    data_stage01_isotopomer_averagesNormSum.scan_type).filter(
                    data_stage01_isotopomer_averagesNormSum.experiment_id.like(experiment_id_I),
                    data_stage01_isotopomer_averagesNormSum.used_.is_(True),
                    data_stage01_isotopomer_averagesNormSum.time_point.like(time_point_I),
                    data_stage01_isotopomer_averagesNormSum.sample_type.like(sample_type_I),
                    data_stage01_isotopomer_averagesNormSum.sample_name_abbreviation.like(sample_name_abbreviations_I)).group_by(
                    data_stage01_isotopomer_averagesNormSum.scan_type).order_by(
                    data_stage01_isotopomer_averagesNormSum.scan_type).all();
            scan_types_O = [];
            for st in scan_types:
                scan_types_O.append(st[0]);
            return scan_types_O;
        except SQLAlchemyError as e:
            print(e);
    # query met_ids  from data_stage01_isotopomer_averagesNormSum
    def get_metIDs_experimentIDAndSampleAbbreviationAndTimePointAndSampleTypeAndScanType_dataStage01AveragesNormSum(self,experiment_id_I,sample_name_abbreviation_I,time_point_I,sample_type_I,scan_type_I):
        '''Querry met ids that are used for the experiment, sample abbreviation, time point, scan type'''
        try:
            met_ids = self.session.query(data_stage01_isotopomer_averagesNormSum.met_id).filter(
                    data_stage01_isotopomer_averagesNormSum.sample_name_abbreviation.like(sample_name_abbreviation_I),
                    data_stage01_isotopomer_averagesNormSum.experiment_id.like(experiment_id_I),
                    data_stage01_isotopomer_averagesNormSum.time_point.like(time_point_I),
                    data_stage01_isotopomer_averagesNormSum.sample_type.like(sample_type_I),
                    data_stage01_isotopomer_averagesNormSum.scan_type.like(scan_type_I),
                    data_stage01_isotopomer_averagesNormSum.used_.is_(True)).group_by(
                    data_stage01_isotopomer_averagesNormSum.met_id).order_by(
                    data_stage01_isotopomer_averagesNormSum.met_id.asc()).all();
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
    # query fragment formulas  from data_stage01_isotopomer_averagesNormSum
    def get_fragmentFormula_experimentIDAndSampleAbbreviationAndTimePointAndSampleTypeAndScanTypeAndMetID_dataStage01AveragesNormSum(self,experiment_id_I,sample_name_abbreviation_I,time_point_I,sample_type_I,scan_type_I,met_id_I):
        '''Querry fragments that are used for the experiment, sample abbreviation, time point, scan type, met id'''
        try:
            fragments = self.session.query(data_stage01_isotopomer_averagesNormSum.fragment_formula).filter(
                    data_stage01_isotopomer_averagesNormSum.sample_name_abbreviation.like(sample_name_abbreviation_I),
                    data_stage01_isotopomer_averagesNormSum.experiment_id.like(experiment_id_I),
                    data_stage01_isotopomer_averagesNormSum.time_point.like(time_point_I),
                    data_stage01_isotopomer_averagesNormSum.sample_type.like(sample_type_I),
                    data_stage01_isotopomer_averagesNormSum.scan_type.like(scan_type_I),
                    data_stage01_isotopomer_averagesNormSum.met_id.like(met_id_I),
                    data_stage01_isotopomer_averagesNormSum.used_.is_(True)).group_by(
                    data_stage01_isotopomer_averagesNormSum.fragment_formula).order_by(
                    data_stage01_isotopomer_averagesNormSum.fragment_formula.asc()).all();
            fragments_O = [];
            if not(fragments):
                print("no results found")
                print("experiment_id_I	sample_name_abbreviation_I	time_point_I	scan_type_I met_id_I");
                print(experiment_id_I,sample_name_abbreviation_I,time_point_I,scan_type_I,met_id_I);
            else:
                for cn in fragments:
                    fragments_O.append(cn[0]);
                return fragments_O;
        except SQLAlchemyError as e:
            print(e);
    # query spectrum from data_stage01_isotopomer_averagesNormSum
    def get_spectrum_experimentIDAndSampleAbbreviationAndTimePointAndSampleTypeAndScanTypeAndMetIDAndFragmentFormula_dataStage01AveragesNormSum(self,experiment_id_I,sample_name_abbreviation_I,time_point_I,sample_type_I,scan_type_I,met_id_I,fragment_formula_I):
        '''Querry fragments that are used for the experiment, sample abbreviation, time point, scan type, met id'''
        try:
            fragments = self.session.query(data_stage01_isotopomer_averagesNormSum.fragment_mass,
                    data_stage01_isotopomer_averagesNormSum.intensity_normalized_average,
                    data_stage01_isotopomer_averagesNormSum.intensity_normalized_cv).filter(
                    data_stage01_isotopomer_averagesNormSum.sample_name_abbreviation.like(sample_name_abbreviation_I),
                    data_stage01_isotopomer_averagesNormSum.experiment_id.like(experiment_id_I),
                    data_stage01_isotopomer_averagesNormSum.time_point.like(time_point_I),
                    data_stage01_isotopomer_averagesNormSum.sample_type.like(sample_type_I),
                    data_stage01_isotopomer_averagesNormSum.scan_type.like(scan_type_I),
                    data_stage01_isotopomer_averagesNormSum.met_id.like(met_id_I),
                    data_stage01_isotopomer_averagesNormSum.fragment_formula.like(fragment_formula_I),
                    data_stage01_isotopomer_averagesNormSum.used_.is_(True)).group_by(
                    data_stage01_isotopomer_averagesNormSum.fragment_mass,
                    data_stage01_isotopomer_averagesNormSum.intensity_normalized_average,
                    data_stage01_isotopomer_averagesNormSum.intensity_normalized_cv).order_by(
                    data_stage01_isotopomer_averagesNormSum.fragment_mass.asc()).all();
            fragment_mass_O = [];
            intensity_normalized_average_O = [];
            intensity_normalized_cv_O = [];
            if not(fragments):
                print("no results found")
                print("experiment_id_I	sample_name_abbreviation_I	time_point_I	scan_type_I met_id_I    fragment_forula_I");
                print(experiment_id_I,sample_name_abbreviation_I,time_point_I,scan_type_I,met_id_I,fragment_forula_I);
            else:
                for cn in fragments:
                    fragment_mass_O.append(cn[0]);
                    intensity_normalized_average_O.append(cn[1]);
                    intensity_normalized_cv_O.append(cn[2]);
                return intensity_normalized_average_O,intensity_normalized_cv_O,fragment_mass_O;
        except SQLAlchemyError as e:
            print(e);
    # query normalized intensity from data_stage01_isotopomer_averagesNormSum
    def get_dataProductFragment_experimentIDAndTimePointSampleAbbreviationAndSampleTypeAndScanTypeAndMetID_dataStage01AveragesNormSum(self,experiment_id_I,sample_name_abbreviation_I,time_point_I,sample_type_I,scan_type_I, met_id_I):
        '''Querry peak data for a specific experiment_id, sample_name_abbreviation'''
        try:
            data = self.session.query(data_stage01_isotopomer_averagesNormSum.fragment_formula,
                    data_stage01_isotopomer_averagesNormSum.fragment_mass,
                    MS_components.product_fragment,
                    data_stage01_isotopomer_averagesNormSum.intensity_normalized_average,
                    data_stage01_isotopomer_averagesNormSum.intensity_normalized_cv,
                    data_stage01_isotopomer_averagesNormSum.intensity_theoretical,
                    data_stage01_isotopomer_averagesNormSum.abs_devFromTheoretical,
                    data_stage01_isotopomer_spectrumAccuracyNormSum.spectrum_accuracy,
                    data_stage01_isotopomer_averagesNormSum.scan_type).filter(
                    data_stage01_isotopomer_averagesNormSum.sample_name_abbreviation.like(sample_name_abbreviation_I),
                    data_stage01_isotopomer_averagesNormSum.experiment_id.like(experiment_id_I),
                    data_stage01_isotopomer_averagesNormSum.time_point.like(time_point_I),
                    data_stage01_isotopomer_averagesNormSum.sample_type.like(sample_type_I),
                    data_stage01_isotopomer_averagesNormSum.scan_type.like(scan_type_I),
                    data_stage01_isotopomer_averagesNormSum.met_id.like(met_id_I),
                    data_stage01_isotopomer_averagesNormSum.fragment_formula.like(MS_components.product_formula),
                    data_stage01_isotopomer_averagesNormSum.met_id.like(MS_components.met_id),
                    MS_components.ms_methodtype.like('tuning'),
                    data_stage01_isotopomer_averagesNormSum.used_,
                    data_stage01_isotopomer_spectrumAccuracyNormSum.sample_name_abbreviation.like(sample_name_abbreviation_I),
                    data_stage01_isotopomer_spectrumAccuracyNormSum.experiment_id.like(experiment_id_I),
                    data_stage01_isotopomer_spectrumAccuracyNormSum.time_point.like(time_point_I),
                    data_stage01_isotopomer_spectrumAccuracyNormSum.sample_type.like(sample_type_I),
                    data_stage01_isotopomer_spectrumAccuracyNormSum.scan_type.like(scan_type_I),
                    data_stage01_isotopomer_spectrumAccuracyNormSum.met_id.like(met_id_I),
                    data_stage01_isotopomer_spectrumAccuracyNormSum.used_.is_(True),
                    data_stage01_isotopomer_spectrumAccuracyNormSum.fragment_formula.like(MS_components.product_formula),
                    data_stage01_isotopomer_spectrumAccuracyNormSum.met_id.like(MS_components.met_id)).group_by(
                    data_stage01_isotopomer_averagesNormSum.fragment_formula,
                    data_stage01_isotopomer_averagesNormSum.fragment_mass,
                    MS_components.product_fragment,
                    data_stage01_isotopomer_averagesNormSum.intensity_normalized_average,
                    data_stage01_isotopomer_averagesNormSum.intensity_normalized_cv,
                    data_stage01_isotopomer_averagesNormSum.intensity_theoretical,
                    data_stage01_isotopomer_averagesNormSum.abs_devFromTheoretical,
                    data_stage01_isotopomer_spectrumAccuracyNormSum.spectrum_accuracy,
                    data_stage01_isotopomer_averagesNormSum.scan_type).order_by(
                    data_stage01_isotopomer_averagesNormSum.fragment_formula.desc(),
                    data_stage01_isotopomer_averagesNormSum.fragment_mass.asc()).all();
            data_O = [];
            if not data:
                print('No normalized intensities found for the following:')
                print('sample_name_abbreviation: ' + sample_name_abbreviation_I);
                return data_O;
            else:
                # algorithm will break there is no data for a0 mass and there are jumps in the a values (i.e. a0 to a2);
                fragment_formula = '';
                fragment_formula_old = '';
                data_cnt = len(data)-1;
                i = 0;
                while i <= data_cnt:
                    fragment_formula_old = data[i].fragment_formula;
                    row_key = [];
                    row_theoretical = [];
                    row_measured = [];
                    row_measured_cv = [];
                    row_measured_dif = [];
                    row_spectrum_accuracy = [];
                    row = [];
                    for a in range(50):
                        if i <= data_cnt:
                            fragment_formula = data[i].fragment_formula;
                            if fragment_formula == fragment_formula_old:
                                if a == 0:
                                    # add key columns
                                    row_key.append(sample_name_abbreviation_I);
                                    row_key.append(time_point_I);
                                    row_key.append(met_id_I);
                                    row_key.append(data[i].fragment_formula);
                                    row_key.append(str(data[i].product_fragment));
                                    row_key.append(data[i].scan_type);
                                    row_spectrum_accuracy.append(data[i].spectrum_accuracy);
                                    mass0 = data[i].fragment_mass
                                massi = data[i].fragment_mass;
                                massDif = massi-mass0;
                                # add a+0... information
                                if data[i].intensity_theoretical: theoretical = numpy.round(data[i].intensity_theoretical,3);
                                else: theoretical = data[i].intensity_theoretical;
                                row_theoretical.append(theoretical)
                                if data[i].intensity_normalized_average: measured = numpy.round(data[i].intensity_normalized_average,3);
                                else: measured = data[i].intensity_normalized_average;
                                row_measured.append(measured)
                                if data[i].intensity_normalized_cv: cv = numpy.round(data[i].intensity_normalized_cv,3);
                                else: cv = data[i].intensity_normalized_cv;
                                row_measured_cv.append(cv);
                                if data[i].abs_devFromTheoretical: dif = numpy.round(data[i].abs_devFromTheoretical,3)
                                else: dif = data[i].abs_devFromTheoretical;
                                row_measured_dif.append(dif)
                                i += 1;
                            else:
                                row_theoretical.append(None);
                                row_measured.append(None);
                                row_measured_cv.append(None);
                                row_measured_dif.append(None);
                        else:
                            row_theoretical.append(None);
                            row_measured.append(None);
                            row_measured_cv.append(None);
                            row_measured_dif.append(None);
                    row.extend(row_key);
                    row.extend(row_theoretical);
                    row.extend(row_measured);
                    row.extend(row_measured_cv);
                    row.extend(row_measured_dif);
                    row.extend(row_spectrum_accuracy);
                    data_O.append(row);
                return data_O;
        except SQLAlchemyError as e:
            print(e);
    def get_dataPrecursorFragment_experimentIDAndTimePointSampleAbbreviationAndSampleTypeAndScanTypeAndMetID_dataStage01AveragesNormSum(self,experiment_id_I,sample_name_abbreviation_I,time_point_I,sample_type_I,scan_type_I, met_id_I):
        '''Querry peak data for a specific experiment_id, sample_name_abbreviation'''
        try:
            data = self.session.query(data_stage01_isotopomer_averagesNormSum.fragment_formula,
                    data_stage01_isotopomer_averagesNormSum.fragment_mass,
                    MS_components.precursor_fragment,
                    data_stage01_isotopomer_averagesNormSum.intensity_normalized_average,
                    data_stage01_isotopomer_averagesNormSum.intensity_normalized_cv,
                    data_stage01_isotopomer_averagesNormSum.intensity_theoretical,
                    data_stage01_isotopomer_averagesNormSum.abs_devFromTheoretical,
                    data_stage01_isotopomer_spectrumAccuracyNormSum.spectrum_accuracy,
                    data_stage01_isotopomer_averagesNormSum.scan_type).filter(
                    data_stage01_isotopomer_averagesNormSum.sample_name_abbreviation.like(sample_name_abbreviation_I),
                    data_stage01_isotopomer_averagesNormSum.experiment_id.like(experiment_id_I),
                    data_stage01_isotopomer_averagesNormSum.time_point.like(time_point_I),
                    data_stage01_isotopomer_averagesNormSum.sample_type.like(sample_type_I),
                    data_stage01_isotopomer_averagesNormSum.scan_type.like(scan_type_I),
                    data_stage01_isotopomer_averagesNormSum.met_id.like(met_id_I),
                    data_stage01_isotopomer_averagesNormSum.fragment_formula.like(MS_components.precursor_formula),
                    data_stage01_isotopomer_averagesNormSum.met_id.like(MS_components.met_id),
                    MS_components.ms_methodtype.like('tuning'),
                    data_stage01_isotopomer_averagesNormSum.used_,
                    data_stage01_isotopomer_spectrumAccuracyNormSum.sample_name_abbreviation.like(sample_name_abbreviation_I),
                    data_stage01_isotopomer_spectrumAccuracyNormSum.experiment_id.like(experiment_id_I),
                    data_stage01_isotopomer_spectrumAccuracyNormSum.time_point.like(time_point_I),
                    data_stage01_isotopomer_spectrumAccuracyNormSum.sample_type.like(sample_type_I),
                    data_stage01_isotopomer_spectrumAccuracyNormSum.scan_type.like(scan_type_I),
                    data_stage01_isotopomer_spectrumAccuracyNormSum.met_id.like(met_id_I),
                    data_stage01_isotopomer_spectrumAccuracyNormSum.used_.is_(True),
                    data_stage01_isotopomer_spectrumAccuracyNormSum.fragment_formula.like(MS_components.precursor_formula),
                    data_stage01_isotopomer_spectrumAccuracyNormSum.met_id.like(MS_components.met_id)).group_by(
                    data_stage01_isotopomer_averagesNormSum.fragment_formula,
                    data_stage01_isotopomer_averagesNormSum.fragment_mass,
                    MS_components.precursor_fragment,
                    data_stage01_isotopomer_averagesNormSum.intensity_normalized_average,
                    data_stage01_isotopomer_averagesNormSum.intensity_normalized_cv,
                    data_stage01_isotopomer_averagesNormSum.intensity_theoretical,
                    data_stage01_isotopomer_averagesNormSum.abs_devFromTheoretical,
                    data_stage01_isotopomer_spectrumAccuracyNormSum.spectrum_accuracy,
                    data_stage01_isotopomer_averagesNormSum.scan_type).order_by(
                    data_stage01_isotopomer_averagesNormSum.fragment_formula.desc(),
                    data_stage01_isotopomer_averagesNormSum.fragment_mass.asc()).all();
            data_O = [];
            if not data:
                print('No normalized intensities found for the following:')
                print('sample_name_abbreviation: ' + sample_name_abbreviation_I);
                return data_O;
            else:
                # algorithm will break there is no data for a0 mass and there are jumps in the a values (i.e. a0 to a2);
                fragment_formula = '';
                fragment_formula_old = '';
                data_cnt = len(data)-1;
                i = 0;
                while i <= data_cnt:
                    fragment_formula_old = data[i].fragment_formula;
                    row_key = [];
                    row_theoretical = [];
                    row_measured = [];
                    row_measured_cv = [];
                    row_measured_dif = [];
                    row_spectrum_accuracy = [];
                    row = [];
                    for a in range(50):
                        if i <= data_cnt:
                            fragment_formula = data[i].fragment_formula;
                            if fragment_formula == fragment_formula_old:
                                if a == 0:
                                    # add key columns
                                    row_key.append(sample_name_abbreviation_I);
                                    row_key.append(time_point_I);
                                    row_key.append(met_id_I);
                                    row_key.append(data[i].fragment_formula);
                                    row_key.append(str(data[i].precursor_fragment));
                                    row_key.append(data[i].scan_type);
                                    row_spectrum_accuracy.append(data[i].spectrum_accuracy);
                                    mass0 = data[i].fragment_mass
                                massi = data[i].fragment_mass;
                                massDif = massi-mass0;
                                # add a+0... information
                                if data[i].intensity_theoretical: theoretical = numpy.round(data[i].intensity_theoretical,3);
                                else: theoretical = data[i].intensity_theoretical;
                                row_theoretical.append(theoretical)
                                if data[i].intensity_normalized_average: measured = numpy.round(data[i].intensity_normalized_average,3);
                                else: measured = data[i].intensity_normalized_average;
                                row_measured.append(measured)
                                if data[i].intensity_normalized_cv: cv = numpy.round(data[i].intensity_normalized_cv,3);
                                else: cv = data[i].intensity_normalized_cv;
                                row_measured_cv.append(cv);
                                if data[i].abs_devFromTheoretical: dif = numpy.round(data[i].abs_devFromTheoretical,3)
                                else: dif = data[i].abs_devFromTheoretical;
                                row_measured_dif.append(dif)
                                i += 1;
                            else:
                                row_theoretical.append(None);
                                row_measured.append(None);
                                row_measured_cv.append(None);
                                row_measured_dif.append(None);
                        else:
                            row_theoretical.append(None);
                            row_measured.append(None);
                            row_measured_cv.append(None);
                            row_measured_dif.append(None);
                    row.extend(row_key);
                    row.extend(row_theoretical);
                    row.extend(row_measured);
                    row.extend(row_measured_cv);
                    row.extend(row_measured_dif);
                    row.extend(row_spectrum_accuracy);
                    data_O.append(row);
                return data_O;
        except SQLAlchemyError as e:
            print(e);
    # query row from data_stage01_isotopomer_averagesNormSum
    def get_dataProductFragment_experimentIDAndSampleAbbreviation_dataStage01AveragesNormSum(self,experiment_id_I,sample_name_abbreviation_I):
        '''Querry peak data for a specific experiment_id, sample_name_abbreviation'''
        try:
            data = self.session.query(data_stage01_isotopomer_averagesNormSum.fragment_formula,
                    data_stage01_isotopomer_averagesNormSum.fragment_mass,
                    data_stage01_isotopomer_averagesNormSum.intensity_normalized_average,
                    data_stage01_isotopomer_averagesNormSum.intensity_normalized_cv,
                    data_stage01_isotopomer_averagesNormSum.intensity_theoretical,
                    data_stage01_isotopomer_averagesNormSum.scan_type,
                    data_stage01_isotopomer_averagesNormSum.experiment_id,
                    data_stage01_isotopomer_averagesNormSum.time_point,
                    data_stage01_isotopomer_averagesNormSum.sample_type,
                    data_stage01_isotopomer_averagesNormSum.met_id,
                    data_stage01_isotopomer_averagesNormSum.sample_name_abbreviation,
                    MS_components.product_fragment).filter(
                    data_stage01_isotopomer_averagesNormSum.sample_name_abbreviation.like(sample_name_abbreviation_I),
                    data_stage01_isotopomer_averagesNormSum.experiment_id.like(experiment_id_I),
                    data_stage01_isotopomer_averagesNormSum.fragment_formula.like(MS_components.product_formula),
                    data_stage01_isotopomer_averagesNormSum.met_id.like(MS_components.met_id),
                    MS_components.ms_methodtype.like('tuning'),
                    data_stage01_isotopomer_averagesNormSum.used_).group_by(
                    data_stage01_isotopomer_averagesNormSum.fragment_formula,
                    data_stage01_isotopomer_averagesNormSum.fragment_mass,
                    data_stage01_isotopomer_averagesNormSum.intensity_normalized_average,
                    data_stage01_isotopomer_averagesNormSum.intensity_normalized_cv,
                    data_stage01_isotopomer_averagesNormSum.intensity_theoretical,
                    data_stage01_isotopomer_averagesNormSum.scan_type,
                    data_stage01_isotopomer_averagesNormSum.experiment_id,
                    data_stage01_isotopomer_averagesNormSum.time_point,
                    data_stage01_isotopomer_averagesNormSum.sample_type,
                    data_stage01_isotopomer_averagesNormSum.met_id,
                    data_stage01_isotopomer_averagesNormSum.sample_name_abbreviation,
                    MS_components.product_fragment).order_by(
                    data_stage01_isotopomer_averagesNormSum.sample_name_abbreviation.asc(),
                    data_stage01_isotopomer_averagesNormSum.sample_type.asc(),
                    data_stage01_isotopomer_averagesNormSum.met_id.asc(),
                    data_stage01_isotopomer_averagesNormSum.fragment_formula.desc(),
                    data_stage01_isotopomer_averagesNormSum.fragment_mass.asc()).all();
            data_O = [];
            if not data:
                print('No normalized intensities found for the following:')
                print('sample_name_abbreviation: ' + sample_name_abbreviation_I);
                return data_O;
            else:
                for d in data:
                    #TODO:
                    data_O.append(d);
                return data_O;
        except SQLAlchemyError as e:
            print(e);
    def get_rows_experimentIDAndSampleAbbreviationAndTimePointAndSampleTypeAndScanTypeAndMetID_dataStage01AveragesNormSum(self,experiment_id_I,sample_name_abbreviation_I,time_point_I,sample_type_I,scan_type_I,met_id_I):
        '''Querry rows that are used for the experiment, sample abbreviation, time point, scan type, met id'''
        try:
            rows = self.session.query(data_stage01_isotopomer_averagesNormSum).filter(
                    data_stage01_isotopomer_averagesNormSum.sample_name_abbreviation.like(sample_name_abbreviation_I),
                    data_stage01_isotopomer_averagesNormSum.experiment_id.like(experiment_id_I),
                    data_stage01_isotopomer_averagesNormSum.time_point.like(time_point_I),
                    data_stage01_isotopomer_averagesNormSum.sample_type.like(sample_type_I),
                    data_stage01_isotopomer_averagesNormSum.scan_type.like(scan_type_I),
                    data_stage01_isotopomer_averagesNormSum.met_id.like(met_id_I),
                    data_stage01_isotopomer_averagesNormSum.used_.is_(True)).all();
            rows_O = [];
            if not(rows):
                print("no results found")
                print("experiment_id_I	sample_name_abbreviation_I	time_point_I	scan_type_I met_id_I");
                print(experiment_id_I,sample_name_abbreviation_I,time_point_I,scan_type_I,met_id_I);
            else:
                for d in rows:
                    rows_O.append({
                        #'id':d.id,
                'experiment_id':d.experiment_id,
                'sample_name_abbreviation':d.sample_name_abbreviation,
                'sample_type':d.sample_type,
                'time_point':d.time_point,
                'met_id':d.met_id,
                'fragment_formula':d.fragment_formula,
                'fragment_mass':d.fragment_mass,
                'intensity_normalized_average':d.intensity_normalized_average,
                'intensity_normalized_cv':d.intensity_normalized_cv,
                'intensity_normalized_units':d.intensity_normalized_units,
                'intensity_theoretical':d.intensity_theoretical,
                'abs_devFromTheoretical':d.abs_devFromTheoretical,
                'scan_type':d.scan_type,
                'used_':d.used_,
                'comment_':d.comment_});
            return rows_O;
        except SQLAlchemyError as e:
            print(e);

    def update_dataStage01IsotopomerAverages_usedAndComment(self,dataListUpdated_I):
        # update used and comment fields of the data_stage01_isotopomer_averages
        for d in dataListUpdated_I:
            try:
                data_update = self.session.query(data_stage01_isotopomer_averages).filter(
                        data_stage01_isotopomer_averages.experiment_id.like(d['experiment_id']),
                        data_stage01_isotopomer_averages.sample_name_abbreviation.like(d['sample_name_abbreviation']),
                        data_stage01_isotopomer_averages.time_point.like(d['time_point']),
                        data_stage01_isotopomer_averages.sample_type.like(d['sample_type']),
                        data_stage01_isotopomer_averages.met_id.like(d['met_id']),
                        data_stage01_isotopomer_averages.fragment_formula.like(d['fragment_formula']),
                        data_stage01_isotopomer_averages.fragment_mass == int(d['fragment_mass']),
                        data_stage01_isotopomer_averages.scan_type.like(d['scan_type'])
                        ).update(		
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

    def update_dataStage01IsotopomerAveragesNormSum_usedAndComment(self,dataListUpdated_I):
        # update used and comment fields of the data_stage01_isotopomer_averagesNormSum
        for d in dataListUpdated_I:
            try:
                data_update = self.session.query(data_stage01_isotopomer_averagesNormSum).filter(
                        data_stage01_isotopomer_averagesNormSum.experiment_id.like(d['experiment_id']),
                        data_stage01_isotopomer_averagesNormSum.sample_name_abbreviation.like(d['sample_name_abbreviation']),
                        data_stage01_isotopomer_averagesNormSum.time_point.like(d['time_point']),
                        data_stage01_isotopomer_averagesNormSum.sample_type.like(d['sample_type']),
                        data_stage01_isotopomer_averagesNormSum.met_id.like(d['met_id']),
                        data_stage01_isotopomer_averagesNormSum.fragment_formula.like(d['fragment_formula']),
                        data_stage01_isotopomer_averagesNormSum.fragment_mass == int(d['fragment_mass']),
                        data_stage01_isotopomer_averagesNormSum.scan_type.like(d['scan_type'])
                        ).update(		
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
