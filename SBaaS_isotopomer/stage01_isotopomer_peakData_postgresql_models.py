from SBaaS_base.postgresql_orm_base import *
class data_stage01_isotopomer_peakData(Base):
    __tablename__ = 'data_stage01_isotopomer_peakData'
    id = Column(Integer, Sequence('data_stage01_isotopomer_peakdata_id_seq'), primary_key=True)
    experiment_id = Column(String(50))
    sample_name = Column(String(100))
    met_id = Column(String(500))
    precursor_formula = Column(String(500))
    mass = Column(Float)
    mass_units = Column(String(20), default='Da')
    intensity = Column(Float)
    intensity_units = Column(String(20), default='cps')
    scan_type = Column(String(50));
    used_ = Column(Boolean);
    comment_ = Column(Text);

    def __init__(self, experiment_id_I, sample_name_I, met_id_I, precursor_formula_I, mass_I, mass_units_I,
                    intensity_I, intensity_units_I, scan_type_I, used_I):
        self.experiment_id = experiment_id_I;
        self.sample_name = sample_name_I;
        self.met_id = met_id_I;
        self.precursor_formula = precursor_formula_I;
        self.mass = mass_I;
        self.mass_units = mass_units_I;
        self.intensity = intensity_I;
        self.intensity_units = intensity_units_I;
        self.scan_type = scan_type_I;
        self.used_ = used_I;

class data_stage01_isotopomer_peakList(Base):
    __tablename__ = 'data_stage01_isotopomer_peakList'
    id = Column(Integer, Sequence('data_stage01_isotopomer_peaklist_id_seq'), primary_key=True)
    experiment_id = Column(String(50))
    sample_name = Column(String(100))
    met_id = Column(String(500))
    precursor_formula = Column(String(500))
    mass = Column(Float)
    mass_units = Column(String(20), default='Da')
    intensity = Column(Float)
    intensity_units = Column(String(20), default='cps')
    centroid_mass = Column(Float)
    centroid_mass_units = Column(String(20), default='Da')
    peak_start = Column(Float)
    peak_start_units = Column(String(20), default='Da')
    peak_stop = Column(Float);
    peak_stop_units = Column(String(20), default='Da')
    resolution = Column(Float);
    scan_type = Column(String(50));
    used_ = Column(Boolean);
    comment_ = Column(Text);

    def __init__(self, experiment_id_I, sample_name_I, met_id_I, precursor_formula_I, mass_I, mass_units_I,
                    intensity_I, intensity_units_I, centroid_mass_I, centroid_mass_units_I,
                    peak_start_I, peak_start_units_I, peak_stop_I, peak_stop_units_I,
                    resolution_I, scan_type_I, used_I):
        self.experiment_id = experiment_id_I;
        self.sample_name = sample_name_I;
        self.met_id = met_id_I;
        self.precursor_formula = precursor_formula_I;
        self.mass = mass_I;
        self.mass_units = mass_units_I;
        self.intensity = intensity_I;
        self.intensity_units = intensity_units_I;
        self.centroid_mass = centroid_mass_I;
        self.centroid_mass_units = centroid_mass_units_I;
        self.peak_start = peak_start_I;
        self.peak_start_units = peak_start_units_I;
        self.peak_stop = peak_stop_I;
        self.peak_stop_units = peak_stop_units_I;
        self.resolution = resolution_I;
        self.scan_type = scan_type_I;
        self.used_ = used_I;