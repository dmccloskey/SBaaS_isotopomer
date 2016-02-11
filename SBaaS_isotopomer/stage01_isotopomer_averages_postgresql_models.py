from SBaaS_base.postgresql_orm_base import *
class data_stage01_isotopomer_averages(Base):
    __tablename__ = 'data_stage01_isotopomer_averages'
    #id = Column(Integer, Sequence('data_stage01_isotopomer_averages_id_seq'), primary_key=True)
    experiment_id = Column(String(50))
    sample_name_abbreviation = Column(String(100))
    sample_type = Column(String(100))
    time_point = Column(String(10))
    met_id = Column(String(100))
    fragment_formula = Column(String(500))
    fragment_mass = Column(Integer)
    n_replicates = Column(Integer)
    intensity_normalized_average = Column(Float)
    intensity_normalized_cv = Column(Float)
    intensity_normalized_units = Column(String(20))
    intensity_theoretical = Column(Float)
    abs_devFromTheoretical = Column(Float)
    scan_type = Column(String(50));
    used_ = Column(Boolean);
    comment_ = Column(Text);

    __table_args__ = (PrimaryKeyConstraint('experiment_id','sample_name_abbreviation','sample_type','met_id','time_point','fragment_formula','fragment_mass','scan_type'),
                      #UniqueConstraint('experiment_id','sample_name_abbreviation','sample_type','met_id','time_point','fragment_formula','fragment_mass','scan_type'),
            )

    def __init__(self, experiment_id_I, sample_name_abbreviation_I,  sample_type_I, time_point_I, met_id_I,fragment_formula_I, fragment_mass_I,
                    n_replicates_I, intensity_normalized_average_I, intensity_normalized_cv_I,
                    intensity_normalized_units_I, intensity_theoretical_I, abs_devFromTheoretical_I, scan_type_I, used_I):
        self.experiment_id = experiment_id_I;
        self.sample_name_abbreviation = sample_name_abbreviation_I;
        self.sample_type = sample_type_I;
        self.time_point = time_point_I;
        self.met_id = met_id_I;
        self.fragment_formula = fragment_formula_I;
        self.fragment_mass = fragment_mass_I;
        self.n_replicates = n_replicates_I;
        self.intensity_normalized_average = intensity_normalized_average_I;
        self.intensity_normalized_cv = intensity_normalized_cv_I;
        self.intensity_normalized_units = intensity_normalized_units_I;
        self.intensity_theoretical = intensity_theoretical_I;
        self.abs_devFromTheoretical = abs_devFromTheoretical_I;
        self.used_ = used_I;
        self.scan_type = scan_type_I;

class data_stage01_isotopomer_averagesNormSum(Base):
    __tablename__ = 'data_stage01_isotopomer_averagesNormSum'

    #TODO:
    #DROP SEQUENCE "data_stage01_isotopomer_averagesNormSum_fragment_mass_seq";

    #CREATE SEQUENCE "data_stage01_isotopomer_averagesNormSum_id_seq"
    #  INCREMENT 1
    #  MINVALUE 1
    #  MAXVALUE 9223372036854775807
    #  START 1
    #  CACHE 1;
    #ALTER TABLE "data_stage01_isotopomer_averagesNormSum_id_seq"
    #  OWNER TO postgres;

    #ALTER TABLE data_stage01_isotopomer_averagesNormSum ADD COLUMN id integer;
    #ALTER TABLE data_stage01_isotopomer_averagesNormSum ALTER COLUMN id SET NOT NULL;

    #ALTER TABLE data_stage01_isotopomer_averagesNormSum
    #  ADD CONSTRAINT data_stage01_isotopomer_averagesNormSum_id_key UNIQUE(id);

    #id = Column(Integer, Sequence('data_stage01_isotopomer_averagesNormSum_id_seq'))
    experiment_id = Column(String(50))
    sample_name_abbreviation = Column(String(100))
    sample_type = Column(String(100))
    time_point = Column(String(10))
    met_id = Column(String(100))
    fragment_formula = Column(String(500))
    fragment_mass = Column(Integer)
    n_replicates = Column(Integer)
    intensity_normalized_average = Column(Float)
    intensity_normalized_cv = Column(Float)
    intensity_normalized_units = Column(String(20))
    intensity_theoretical = Column(Float)
    abs_devFromTheoretical = Column(Float)
    scan_type = Column(String(50));
    used_ = Column(Boolean);
    comment_ = Column(Text);

    __table_args__ = (PrimaryKeyConstraint('experiment_id','sample_name_abbreviation','sample_type','met_id','time_point','fragment_formula','fragment_mass','scan_type'),
                      #UniqueConstraint('id'),
            )

    def __init__(self, experiment_id_I, sample_name_abbreviation_I,  sample_type_I, time_point_I, met_id_I,fragment_formula_I, fragment_mass_I,
                    n_replicates_I, intensity_normalized_average_I, intensity_normalized_cv_I,
                    intensity_normalized_units_I, intensity_theoretical_I, abs_devFromTheoretical_I, scan_type_I, used_I, comment_I=None):
        self.experiment_id = experiment_id_I;
        self.sample_name_abbreviation = sample_name_abbreviation_I;
        self.sample_type = sample_type_I;
        self.time_point = time_point_I;
        self.met_id = met_id_I;
        self.fragment_formula = fragment_formula_I;
        self.fragment_mass = fragment_mass_I;
        self.n_replicates = n_replicates_I;
        self.intensity_normalized_average = intensity_normalized_average_I;
        self.intensity_normalized_cv = intensity_normalized_cv_I;
        self.intensity_normalized_units = intensity_normalized_units_I;
        self.intensity_theoretical = intensity_theoretical_I;
        self.abs_devFromTheoretical = abs_devFromTheoretical_I;
        self.used_ = used_I;
        self.scan_type = scan_type_I;
        self.comment_ = comment_I;

    def __repr__dict__(self):
        return {
                #'id':self.id,
                'experiment_id':self.experiment_id,
                'sample_name_abbreviation':self.sample_name_abbreviation,
                'sample_type':self.sample_type,
                'time_point':self.time_point,
                'met_id':self.met_id,
                'fragment_formula':self.fragment_formula,
                'fragment_mass':self.fragment_mass,
                'intensity_normalized_average':self.intensity_normalized_average,
                'intensity_normalized_cv':self.intensity_normalized_cv,
                'intensity_normalized_units':self.intensity_normalized_units,
                'intensity_theoretical':self.intensity_theoretical,
                'abs_devFromTheoretical':self.abs_devFromTheoretical,
                'scan_type':self.scan_type,
                'used_':self.used_,
                'comment_':self.comment_}
    
    def __repr__json__(self):
        return json.dumps(self.__repr__dict__())