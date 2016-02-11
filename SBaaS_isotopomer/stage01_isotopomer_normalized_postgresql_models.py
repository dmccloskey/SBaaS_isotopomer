from SBaaS_base.postgresql_orm_base import *
class data_stage01_isotopomer_normalized(Base):
    __tablename__ = 'data_stage01_isotopomer_normalized'
    id = Column(Integer, Sequence('data_stage01_isotopomer_normalized_id_seq'), primary_key=True)
    experiment_id = Column(String(50))
    sample_name = Column(String(100))
    sample_name_abbreviation = Column(String(100))
    sample_type = Column(String(100))
    time_point = Column(String(10))
    dilution = Column(Float)
    replicate_number = Column(Integer)
    met_id = Column(String(100))
    fragment_formula = Column(String(500))
    fragment_mass = Column(Integer)
    intensity = Column(Float)
    intensity_units = Column(String(20))
    intensity_corrected = Column(Float)
    intensity_corrected_units = Column(String(20))
    intensity_normalized = Column(Float)
    intensity_normalized_units = Column(String(20))
    intensity_theoretical = Column(Float)
    abs_devFromTheoretical = Column(Float)
    scan_type = Column(String(50));
    used_ = Column(Boolean);
    comment_ = Column(Text);

    __table_args__ = (UniqueConstraint('experiment_id','sample_name','sample_type','met_id','time_point','fragment_formula','fragment_mass','scan_type'),
            )

    def __init__(self, experiment_id_I, sample_name_I, sample_name_abbreviation_I, sample_type_I,
                 time_point_I, dilution_I, replicate_number_I, met_id_I,
                 fragment_formula_I, fragment_mass_I, intensity_I, intensity_units_I,
                 intensity_corrected_I, intensity_corrected_units_I, intensity_normalized_I, intensity_normalized_units_I,
                 intensity_theoretical_I, abs_devFromTheoretical_I, scan_type_I, used_I,comment_I):
        self.experiment_id = experiment_id_I;
        self.sample_name = sample_name_I;
        self.sample_name_abbreviation = sample_name_abbreviation_I;
        self.sample_type = sample_type_I;
        self.time_point = time_point_I;
        self.dilution = dilution_I;
        self.replicate_number = replicate_number_I;
        self.met_id = met_id_I;
        self.fragment_formula = fragment_formula_I;
        self.fragment_mass = fragment_mass_I;
        self.intensity = intensity_I;
        self.intensity_units = intensity_units_I;
        self.intensity_corrected = intensity_corrected_I;
        self.intensity_corrected_units = intensity_corrected_units_I;
        self.intensity_normalized = intensity_normalized_I;
        self.intensity_normalized_units = intensity_normalized_units_I;
        self.intensity_theoretical = intensity_theoretical_I;
        self.abs_devFromTheoretical = abs_devFromTheoretical_I;
        self.scan_type = scan_type_I;
        self.used_ = used_I;
        self.comment_ = comment_I;

    def __repr__dict__(self):
        return {'id':self.id,
            'experiment_id':self.experiment_id,
                'sample_name':self.sample_name,
                'sample_name_abbreviation':self.sample_name_abbreviation,
                'sample_type':self.sample_type,
                'time_point':self.time_point,
                'dilution':self.dilution,
                'replicate_number':self.replicate_number,
                'met_id':self.met_id,
                'fragment_formula':self.fragment_formula,
                'fragment_mass':self.fragment_mass,
                'intensity':self.intensity,
                'intensity_units':self.intensity_units,
                'intensity_corrected':self.intensity_corrected,
                'intensity_corrected_units':self.intensity_corrected_units,
                'intensity_normalized':self.intensity_normalized,
                'intensity_normalized_units':self.intensity_normalized_units,
                'intensity_theoretical':self.intensity_theoretical,
                'abs_devFromTheoretical':self.abs_devFromTheoretical,
                'scan_type':self.scan_type,
                'used_':self.used_,
                'comment_':self.comment_}
    
    def __repr__json__(self):
        return json.dumps(self.__repr__dict__())