from SBaaS_base.postgresql_orm_base import *
class data_stage01_isotopomer_spectrumAccuracy(Base):
    __tablename__ = 'data_stage01_isotopomer_spectrumAccuracy'
    experiment_id = Column(String(50), primary_key=True)
    sample_name_abbreviation = Column(String(100), primary_key=True)
    sample_type = Column(String(100), primary_key=True)
    time_point = Column(String(10), primary_key=True)
    met_id = Column(String(100), primary_key=True)
    fragment_formula = Column(String(500), primary_key=True)
    spectrum_accuracy = Column(Float)
    scan_type = Column(String(50), primary_key=True);
    used_ = Column(Boolean);
    comment_ = Column(Text);

    def __init__(self, experiment_id_I, sample_name_abbreviation_I,  sample_type_I, time_point_I, met_id_I,fragment_formula_I,
                    spectrum_accuracy_I, scan_type_I, used_I):
        self.experiment_id = experiment_id_I;
        self.sample_name_abbreviation = sample_name_abbreviation_I;
        self.sample_type = sample_type_I;
        self.time_point = time_point_I;
        self.met_id = met_id_I;
        self.fragment_formula = fragment_formula_I;
        self.spectrum_accuracy = spectrum_accuracy_I;
        self.used_ = used_I;
        self.scan_type = scan_type_I;
class data_stage01_isotopomer_spectrumAccuracyNormSum(Base):
    __tablename__ = 'data_stage01_isotopomer_spectrumAccuracyNormSum'
    experiment_id = Column(String(50), primary_key=True)
    sample_name_abbreviation = Column(String(100), primary_key=True)
    sample_type = Column(String(100), primary_key=True)
    time_point = Column(String(10), primary_key=True)
    met_id = Column(String(100), primary_key=True)
    fragment_formula = Column(String(500), primary_key=True)
    spectrum_accuracy = Column(Float)
    scan_type = Column(String(50), primary_key=True);
    used_ = Column(Boolean);
    comment_ = Column(Text);

    def __init__(self, experiment_id_I, sample_name_abbreviation_I,  sample_type_I, time_point_I, met_id_I,fragment_formula_I,
                    spectrum_accuracy_I, scan_type_I, used_I):
        self.experiment_id = experiment_id_I;
        self.sample_name_abbreviation = sample_name_abbreviation_I;
        self.sample_type = sample_type_I;
        self.time_point = time_point_I;
        self.met_id = met_id_I;
        self.fragment_formula = fragment_formula_I;
        self.spectrum_accuracy = spectrum_accuracy_I;
        self.used_ = used_I;
        self.scan_type = scan_type_I;