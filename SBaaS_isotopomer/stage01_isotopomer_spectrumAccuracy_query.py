from .stage01_isotopomer_spectrumAccuracy_postgresql_models import *

from SBaaS_base.sbaas_base_query_update import sbaas_base_query_update
from SBaaS_base.sbaas_base_query_drop import sbaas_base_query_drop
from SBaaS_base.sbaas_base_query_initialize import sbaas_base_query_initialize
from SBaaS_base.sbaas_base_query_insert import sbaas_base_query_insert
from SBaaS_base.sbaas_base_query_select import sbaas_base_query_select
from SBaaS_base.sbaas_base_query_delete import sbaas_base_query_delete

from SBaaS_base.sbaas_template_query import sbaas_template_query

class stage01_isotopomer_spectrumAccuracy_query(sbaas_template_query):
    def initialize_supportedTables(self):
        '''Set the supported tables dict for 
        '''
        tables_supported = {'data_stage01_isotopomer_spectrumAccuracy':data_stage01_isotopomer_spectrumAccuracy,
            'data_stage01_isotopomer_spectrumAccuracyNormSum':data_stage01_isotopomer_spectrumAccuracyNormSum,
                        };
        self.set_supportedTables(tables_supported);
    def initialize_dataStage01_isotopomer_spectrumAccuracy(self):
        try:
            data_stage01_isotopomer_spectrumAccuracy.__table__.create(self.engine,True);
            data_stage01_isotopomer_spectrumAccuracyNormSum.__table__.create(self.engine,True);
        except SQLAlchemyError as e:
            print(e);
    def drop_dataStage01_isotopomer_spectrumAccuracy(self):
        try:
            data_stage01_isotopomer_spectrumAccuracy.__table__.drop(self.engine,True);
            data_stage01_isotopomer_spectrumAccuracyNormSum.__table__.drop(self.engine,True);
        except SQLAlchemyError as e:
            print(e);