from SBaaS_base.postgresql_orm_base import *
class data_stage01_isotopomer_peakSpectrum(Base):
    __tablename__ = 'data_stage01_isotopomer_peakSpectrum'
    id = Column(Integer, Sequence('data_stage01_isotopomer_peakSpectrum_id_seq'), primary_key=True)
    experiment_id = Column(String(50))
    sample_name = Column(String(100))
    sample_name_abbreviation = Column(String(100))
    sample_type = Column(String(100))
    time_point = Column(String(10))
    replicate_number = Column(Integer)
    met_id = Column(String(100))
    precursor_formula = Column(String(500))
    precursor_mass = Column(Integer)#Column(Float)
    product_formula = Column(String(500))
    product_mass = Column(Integer)#Column(Float)
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

    def __init__(self, experiment_id_I, sample_name_I, sample_name_abbreviation_I, sample_type_I, time_point_I, replicate_number_I, met_id_I,
                 precursor_formula_I, precursor_mass_I, product_formula_I, product_mass_I, intensity_I, intensity_units_I,
                 intensity_corrected_I, intensity_corrected_units_I, intensity_normalized_I, intensity_normalized_units_I,
                 intensity_theoretical_I, abs_devFromTheoretical_I, scan_type_I, used_I, comment_I):
        self.experiment_id = experiment_id_I;
        self.sample_name = sample_name_I;
        self.sample_name_abbreviation = sample_name_abbreviation_I;
        self.sample_type = sample_type_I;
        self.time_point = time_point_I;
        self.replicate_number = replicate_number_I;
        self.met_id = met_id_I;
        self.precursor_formula = precursor_formula_I;
        self.precursor_mass = precursor_mass_I;
        self.product_formula = product_formula_I;
        self.product_mass = product_mass_I;
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