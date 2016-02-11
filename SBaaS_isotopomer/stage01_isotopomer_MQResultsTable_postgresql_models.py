from SBaaS_base.postgresql_orm_base import *

class data_stage01_isotopomer_MQResultsTable(Base):
    __tablename__ = 'data_stage01_isotopomer_mqresultstable'
    index_=Column(Integer);
    sample_index=Column(Integer);
    original_filename=Column(Text);
    sample_name=Column(String(100),nullable=False, primary_key=True);
    sample_id=Column(String(500));
    sample_comment=Column(Text);
    sample_type=Column(String(20));
    acquisition_date_and_time=Column(DateTime,nullable=False, primary_key=True);
    rack_number=Column(Integer);
    plate_number=Column(Integer);
    vial_number=Column(Integer);
    dilution_factor=Column(Float);
    injection_volume=Column(Float);
    operator_name=Column(String(100));
    acq_method_name=Column(String(100));
    is_=Column(Boolean);
    component_name=Column(String(500),nullable=False, primary_key=True);
    component_index=Column(Integer);
    component_comment=Column(Text);
    is_comment=Column(Text);
    mass_info=Column(String(100));
    is_mass=Column(String(100));
    is_name=Column(String(500));
    component_group_name=Column(String(100));
    conc_units=Column(String(20));
    failed_query=Column(Boolean);
    is_failed_query=Column(Boolean);
    peak_comment=Column(Text);
    is_peak_comment=Column(Text);
    actual_concentration=Column(Float);
    is_actual_concentration=Column(Float);
    concentration_ratio=Column(Float);
    expected_rt=Column(Float);
    is_expected_rt=Column(Float);
    integration_type=Column(String(100));
    is_integration_type=Column(String(100));
    area=Column(Float);
    is_area=Column(Float);
    corrected_area=Column(Float);
    is_corrected_area=Column(Float);
    area_ratio=Column(Float);
    height=Column(Float);
    is_height=Column(Float);
    corrected_height=Column(Float);
    is_corrected_height=Column(Float);
    height_ratio=Column(Float);
    area_2_height=Column(Float);
    is_area_2_height=Column(Float);
    corrected_area2height=Column(Float);
    is_corrected_area2height=Column(Float);
    region_height=Column(Float);
    is_region_height=Column(Float);
    quality=Column(Float);
    is_quality=Column(Float);
    retention_time=Column(Float);
    is_retention_time=Column(Float);
    start_time=Column(Float);
    is_start_time=Column(Float);
    end_time=Column(Float);
    is_end_time=Column(Float);
    total_width=Column(Float);
    is_total_width=Column(Float);
    width_at_50=Column(Float);
    is_width_at_50=Column(Float);
    signal_2_noise=Column(Float);
    is_signal_2_noise=Column(Float);
    baseline_delta_2_height=Column(Float);
    is_baseline_delta_2_height=Column(Float);
    modified_=Column(Boolean);
    relative_rt=Column(Float);
    used_=Column(Boolean);
    calculated_concentration=Column(Float);
    accuracy_=Column(Float);
    comment_=Column(Text);
    use_calculated_concentration=Column(Boolean,default=True);

    #__table_args__ = (
    #        UniqueConstraint('component_name','sample_name','acquisition_date_and_time'),
    #        )

    def __init__(self,index__I,sample_index_I,original_filename_I,
                 sample_name_I,sample_id_I,sample_comment_I,sample_type_I,
                 acquisition_date_and_time_I,rack_number_I,plate_number_I,
                 vial_number_I,dilution_factor_I,injection_volume_I,
                 operator_name_I,acq_method_name_I,is__I,component_name_I,
                 component_index_I,component_comment_I,is_comment_I,
                 mass_info_I,is_mass_I,is_name_I,component_group_name_I,
                 conc_units_I,failed_query_I,is_failed_query_I,peak_comment_I,
                 is_peak_comment_I,actual_concentration_I,is_actual_concentration_I,
                 concentration_ratio_I,expected_rt_I,is_expected_rt_I,
                 integration_type_I,is_integration_type_I,area_I,is_area_I,
                 corrected_area_I,is_corrected_area_I,area_ratio_I,height_I,
                 is_height_I,corrected_height_I,is_corrected_height_I,
                 height_ratio_I,area_2_height_I,is_area_2_height_I,
                 corrected_area2height_I,is_corrected_area2height_I,
                 region_height_I,is_region_height_I,quality_I,is_quality_I,
                 retention_time_I,is_retention_time_I,start_time_I,
                 is_start_time_I,end_time_I,is_end_time_I,total_width_I,
                 is_total_width_I,width_at_50_I,is_width_at_50_I,
                 signal_2_noise_I,is_signal_2_noise_I,baseline_delta_2_height_I,
                 is_baseline_delta_2_height_I,modified__I,relative_rt_I,used__I,
                 calculated_concentration_I,accuracy__I,comment__I,use_calculated_concentration_I):
        self.index_=index__I;
        self.sample_index=sample_index_I;
        self.original_filename=original_filename_I;
        self.sample_name=sample_name_I;
        self.sample_id=sample_id_I;
        self.sample_comment=sample_comment_I;
        self.sample_type=sample_type_I;
        self.acquisition_date_and_time=acquisition_date_and_time_I;
        self.rack_number=rack_number_I;
        self.plate_number=plate_number_I;
        self.vial_number=vial_number_I;
        self.dilution_factor=dilution_factor_I;
        self.injection_volume=injection_volume_I;
        self.operator_name=operator_name_I;
        self.acq_method_name=acq_method_name_I;
        self.is_=is__I;
        self.component_name=component_name_I;
        self.component_index=component_index_I;
        self.component_comment=component_comment_I;
        self.is_comment=is_comment_I;
        self.mass_info=mass_info_I;
        self.is_mass=is_mass_I;
        self.is_name=is_name_I;
        self.component_group_name=component_group_name_I;
        self.conc_units=conc_units_I;
        self.failed_query=failed_query_I;
        self.is_failed_query=is_failed_query_I;
        self.peak_comment=peak_comment_I;
        self.is_peak_comment=is_peak_comment_I;
        self.actual_concentration=actual_concentration_I;
        self.is_actual_concentration=is_actual_concentration_I;
        self.concentration_ratio=concentration_ratio_I;
        self.expected_rt=expected_rt_I;
        self.is_expected_rt=is_expected_rt_I;
        self.integration_type=integration_type_I;
        self.is_integration_type=is_integration_type_I;
        self.area=area_I;
        self.is_area=is_area_I;
        self.corrected_area=corrected_area_I;
        self.is_corrected_area=is_corrected_area_I;
        self.area_ratio=area_ratio_I;
        self.height=height_I;
        self.is_height=is_height_I;
        self.corrected_height=corrected_height_I;
        self.is_corrected_height=is_corrected_height_I;
        self.height_ratio=height_ratio_I;
        self.area_2_height=area_2_height_I;
        self.is_area_2_height=is_area_2_height_I;
        self.corrected_area2height=corrected_area2height_I;
        self.is_corrected_area2height=is_corrected_area2height_I;
        self.region_height=region_height_I;
        self.is_region_height=is_region_height_I;
        self.quality=quality_I;
        self.is_quality=is_quality_I;
        self.retention_time=retention_time_I;
        self.is_retention_time=is_retention_time_I;
        self.start_time=start_time_I;
        self.is_start_time=is_start_time_I;
        self.end_time=end_time_I;
        self.is_end_time=is_end_time_I;
        self.total_width=total_width_I;
        self.is_total_width=is_total_width_I;
        self.width_at_50=width_at_50_I;
        self.is_width_at_50=is_width_at_50_I;
        self.signal_2_noise=signal_2_noise_I;
        self.is_signal_2_noise=is_signal_2_noise_I;
        self.baseline_delta_2_height=baseline_delta_2_height_I;
        self.is_baseline_delta_2_height=is_baseline_delta_2_height_I;
        self.modified_=modified__I;
        self.relative_rt=relative_rt_I;
        self.used_=used__I;
        self.calculated_concentration=calculated_concentration_I;
        self.accuracy_=accuracy__I;
        self.comment_=comment__I;
        self.use_calculated_concentration=use_calculated_concentration_I;

    #TODO:
    #define relations

    #define representation
    def __repr__(self):
        return "data_stage01_quantification_MQResultsTable %s" % (self.acquisition_date_and_time, self.sample_name,self.component_name)

    def __repr__dict__(self):
        return {'index_':self.index_,
            'sample_index':self.sample_index,
            'original_filename':self.original_filename,
            'sample_name':self.sample_name,
            'sample_id':self.sample_id,
            'sample_comment':self.sample_comment,
            'sample_type':self.sample_type,
            'acquisition_date_and_time':self.acquisition_date_and_time,
            'rack_number':self.rack_number,
            'plate_number':self.plate_number,
            'vial_number':self.vial_number,
            'dilution_factor':self.dilution_factor,
            'injection_volume':self.injection_volume,
            'operator_name':self.operator_name,
            'acq_method_name':self.acq_method_name,
            'is_':self.is_,
            'component_name':self.component_name,
            'component_index':self.component_index,
            'component_comment':self.component_comment,
            'is_comment':self.is_comment,
            'mass_info':self.mass_info,
            'is_mass':self.is_mass,
            'is_name':self.is_name,
            'component_group_name':self.component_group_name,
            'conc_units':self.conc_units,
            'failed_query':self.failed_query,
            'is_failed_query':self.is_failed_query,
            'peak_comment':self.peak_comment,
            'is_peak_comment':self.is_peak_comment,
            'actual_concentration':self.actual_concentration,
            'is_actual_concentration':self.is_actual_concentration,
            'concentration_ratio':self.concentration_ratio,
            'expected_rt':self.expected_rt,
            'is_expected_rt':self.is_expected_rt,
            'integration_type':self.integration_type,
            'is_integration_type':self.is_integration_type,
            'area':self.area,
            'is_area':self.is_area,
            'corrected_area':self.corrected_area,
            'is_corrected_area':self.is_corrected_area,
            'area_ratio':self.area_ratio,
            'height':self.height,
            'is_height':self.is_height,
            'corrected_height':self.corrected_height,
            'is_corrected_height':self.is_corrected_height,
            'height_ratio':self.height_ratio,
            'area_2_height':self.area_2_height,
            'is_area_2_height':self.is_area_2_height,
            'corrected_area2height':self.corrected_area2height,
            'is_corrected_area2height':self.is_corrected_area2height,
            'region_height':self.region_height,
            'is_region_height':self.is_region_height,
            'quality':self.quality,
            'is_quality':self.is_quality,
            'retention_time':self.retention_time,
            'is_retention_time':self.is_retention_time,
            'start_time':self.start_time,
            'is_start_time':self.is_start_time,
            'end_time':self.end_time,
            'is_end_time':self.is_end_time,
            'total_width':self.total_width,
            'is_total_width':self.is_total_width,
            'width_at_50':self.width_at_50,
            'is_width_at_50':self.is_width_at_50,
            'signal_2_noise':self.signal_2_noise,
            'is_signal_2_noise':self.is_signal_2_noise,
            'baseline_delta_2_height':self.baseline_delta_2_height,
            'is_baseline_delta_2_height':self.is_baseline_delta_2_height,
            'modified_':self.modified_,
            'relative_rt':self.relative_rt,
            'used_':self.used_,
            'calculated_concentration':self.calculated_concentration,
            'accuracy_':self.accuracy_,
            'comment_':self.comment_,
            'use_calculated_concentration':self.use_calculated_concentration,
            }
    
    def __repr__json__(self):
        return json.dumps(self.__repr__dict__())