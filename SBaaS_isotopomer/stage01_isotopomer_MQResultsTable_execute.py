
from .stage01_isotopomer_MQResultsTable_io import stage01_isotopomer_MQResultsTable_io

class stage01_isotopomer_MQResultsTable_execute(stage01_isotopomer_MQResultsTable_io):
    # data_stage01_isotopomer deletes
    def execute_deleteExperimentFromMQResultsTable(self,experiment_id_I,sample_types_I = ['Quality Control','Unknown']):
        '''delete rows in data_stage01_MQResultsTable by sample name and sample type 
        (default = Quality Control and Unknown) from the experiment'''
        
        print('deleting rows in data_stage01_MQResultsTable by sample_name and sample_type...');
        dataDeletes = [];
        # get sample_names
        sample_names = [];
        for st in sample_types_I:
            sample_names_tmp = [];
            sample_names_tmp = self.get_allSampleNames_experimentIDAndSampleType(experiment_id_I,st);
            sample_names.extend(sample_names_tmp);
        for sn in sample_names:
            # format into a dictionary list
            print('deleting sample_name ' + sn);
            dataDeletes.append({'sample_name':sn});
        # delete rows based on sample_names
        self.delete_row_sampleName(dataDeletes);

    