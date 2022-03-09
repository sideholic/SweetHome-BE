from django.db import models


# Create your models here.
class Info(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    answer = models.IntegerField()


class News(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    createdAt = models.DateTimeField()
    updatedAt = models.DateTimeField()
    isDelete = models.BooleanField()


class Apt(models.Model):
    HOUSE_MANAGE_NO = models.IntegerField(primary_key=True)
    BSNS_MBY_NM = models.CharField(max_length=100, null=True)
    CNSTRCT_ENTRPS_NM = models.CharField(max_length=100, null=True)
    CNTRCT_CNCLS_BGNDE = models.CharField(max_length=100, null=True)
    CNTRCT_CNCLS_ENDDE = models.CharField(max_length=100, null=True)
    GNRL_RNK1_CRSPAREA_RCEPT_PD = models.CharField(max_length=100, null=True)
    GNRL_RNK1_ETC_AREA_RCPTDE_PD = models.CharField(max_length=100, null=True)
    GNRL_RNK1_ETC_GG_RCPTDE_PD = models.CharField(max_length=100, null=True)
    GNRL_RNK2_CRSPAREA_RCEPT_PD = models.CharField(max_length=100, null=True)
    GNRL_RNK2_ETC_AREA_RCPTDE_PD = models.CharField(max_length=100, null=True)
    GNRL_RNK2_ETC_GG_RCPTDE_PD = models.CharField(max_length=100, null=True)
    HMPG_ADRES = models.CharField(max_length=100, null=True)
    HOUSE_DTL_SECD = models.CharField(max_length=100, null=True)
    HOUSE_DTL_SECD_NM = models.CharField(max_length=100, null=True)
    HOUSE_NM = models.CharField(max_length=100, null=True)
    HOUSE_SECD = models.CharField(max_length=100, null=True)
    HOUSE_SECD_NM = models.CharField(max_length=100, null=True)
    HSSPLY_ADRES = models.CharField(max_length=100, null=True)
    HSSPLY_ZIP = models.CharField(max_length=100, null=True)
    IMPRMN_BSNS_AT = models.CharField(max_length=100, null=True)
    LRSCL_BLDLND_AT = models.CharField(max_length=100, null=True)
    MDAT_TRGET_AREA_SECD = models.CharField(max_length=100, null=True)
    MDHS_TELNO = models.CharField(max_length=100, null=True)
    MVN_PREARNGE_YM = models.CharField(max_length=100, null=True)
    NPLN_PRVOPR_PUBLIC_HOUSE_AT = models.CharField(max_length=100, null=True)
    PARCPRC_ULS_AT = models.CharField(max_length=100, null=True)
    PBLANC_NO = models.IntegerField()
    PRZWNER_PRESNATN_DE = models.CharField(max_length=100, null=True)
    PUBLIC_HOUSE_EARTH_AT = models.CharField(max_length=100, null=True)
    RCEPT_BGNDE = models.CharField(max_length=100, null=True)
    RCEPT_ENDDE = models.CharField(max_length=100, null=True)
    RCRIT_PBLANC_DE = models.CharField(max_length=100, null=True)
    RENT_SECD = models.CharField(max_length=100, null=True)
    RENT_SECD_NM = models.CharField(max_length=100, null=True)
    SPECLT_RDN_EARTH_AT = models.CharField(max_length=100, null=True)
    SPSPLY_RCEPT_BGNDE = models.CharField(max_length=100, null=True)
    SPSPLY_RCEPT_ENDDE = models.CharField(max_length=100, null=True)
    SUBSCRPT_AREA_CODE = models.CharField(max_length=100, null=True)
    SUBSCRPT_AREA_CODE_NM = models.CharField(max_length=100, null=True)
    TOT_SUPLY_HSHLDCO = models.IntegerField()

    def from_json(self, json):
        self.BSNS_MBY_NM = json['BSNS_MBY_NM']
        self.CNSTRCT_ENTRPS_NM = json['CNSTRCT_ENTRPS_NM']
        self.CNTRCT_CNCLS_BGNDE = json['CNTRCT_CNCLS_BGNDE']
        self.CNTRCT_CNCLS_ENDDE = json['CNTRCT_CNCLS_ENDDE']
        self.GNRL_RNK1_CRSPAREA_RCEPT_PD = json['GNRL_RNK1_CRSPAREA_RCEPT_PD']
        self.GNRL_RNK1_ETC_AREA_RCPTDE_PD = json['GNRL_RNK1_ETC_AREA_RCPTDE_PD']
        self.GNRL_RNK1_ETC_GG_RCPTDE_PD = json['GNRL_RNK1_ETC_GG_RCPTDE_PD']
        self.GNRL_RNK2_CRSPAREA_RCEPT_PD = json['GNRL_RNK2_CRSPAREA_RCEPT_PD']
        self.GNRL_RNK2_ETC_AREA_RCPTDE_PD = json['GNRL_RNK2_ETC_AREA_RCPTDE_PD']
        self.GNRL_RNK2_ETC_GG_RCPTDE_PD = json['GNRL_RNK2_ETC_GG_RCPTDE_PD']
        self.HMPG_ADRES = json['HMPG_ADRES']
        self.HOUSE_DTL_SECD = json['HOUSE_DTL_SECD']
        self.HOUSE_DTL_SECD_NM = json['HOUSE_DTL_SECD_NM']
        self.HOUSE_MANAGE_NO = json['HOUSE_MANAGE_NO']
        self.HOUSE_NM = json['HOUSE_NM']
        self.HOUSE_SECD = json['HOUSE_SECD']
        self.HOUSE_SECD_NM = json['HOUSE_SECD_NM']
        self.HSSPLY_ADRES = json['HSSPLY_ADRES']
        self.HSSPLY_ZIP = json['HSSPLY_ZIP']
        self.IMPRMN_BSNS_AT = json['IMPRMN_BSNS_AT']
        self.LRSCL_BLDLND_AT = json['LRSCL_BLDLND_AT']
        self.MDAT_TRGET_AREA_SECD = json['MDAT_TRGET_AREA_SECD']
        self.MDHS_TELNO = json['MDHS_TELNO']
        self.MVN_PREARNGE_YM = json['MVN_PREARNGE_YM']
        self.NPLN_PRVOPR_PUBLIC_HOUSE_AT = json['NPLN_PRVOPR_PUBLIC_HOUSE_AT']
        self.PARCPRC_ULS_AT = json['PARCPRC_ULS_AT']
        self.PBLANC_NO = json['PBLANC_NO']
        self.PRZWNER_PRESNATN_DE = json['PRZWNER_PRESNATN_DE']
        self.PUBLIC_HOUSE_EARTH_AT = json['PUBLIC_HOUSE_EARTH_AT']
        self.RCEPT_BGNDE = json['RCEPT_BGNDE']
        self.RCEPT_ENDDE = json['RCEPT_ENDDE']
        self.RCRIT_PBLANC_DE = json['RCRIT_PBLANC_DE']
        self.RENT_SECD = json['RENT_SECD']
        self.RENT_SECD_NM = json['RENT_SECD_NM']
        self.SPECLT_RDN_EARTH_AT = json['SPECLT_RDN_EARTH_AT']
        self.SPSPLY_RCEPT_BGNDE = json['SPSPLY_RCEPT_BGNDE']
        self.SPSPLY_RCEPT_ENDDE = json['SPSPLY_RCEPT_ENDDE']
        self.SUBSCRPT_AREA_CODE = json['SUBSCRPT_AREA_CODE']
        self.SUBSCRPT_AREA_CODE_NM = json['SUBSCRPT_AREA_CODE_NM']
        self.TOT_SUPLY_HSHLDCO = json['TOT_SUPLY_HSHLDCO']
        return self


class Urbty(models.Model):
    BSNS_MBY_NM = models.TextField(null=True)
    CNTRCT_CNCLS_BGNDE = models.TextField(null=True)
    CNTRCT_CNCLS_ENDDE = models.TextField(null=True)
    HMPG_ADRES = models.TextField(null=True)
    HOUSE_DTL_SECD = models.TextField(null=True)
    HOUSE_DTL_SECD_NM = models.TextField(null=True)
    HOUSE_MANAGE_NO = models.IntegerField(null=True)
    HOUSE_NM = models.TextField(null=True)
    HOUSE_SECD = models.TextField(null=True)
    HOUSE_SECD_NM = models.TextField(null=True)
    HSSPLY_ADRES = models.TextField(null=True)
    HSSPLY_ZIP = models.TextField(null=True)
    MDHS_TELNO = models.TextField(null=True)
    MVN_PREARNGE_YM = models.TextField(null=True)
    PBLANC_NO = models.IntegerField(primary_key=True)
    PRZWNER_PRESNATN_DE = models.TextField(null=True)
    RCRIT_PBLANC_DE = models.TextField(null=True)
    SEARCH_HOUSE_SECD = models.TextField(null=True)
    SUBSCRPT_RCEPT_BGNDE = models.TextField(null=True)
    SUBSCRPT_RCEPT_ENDDE = models.TextField(null=True)
    TOT_SUPLY_HSHLDCO = models.IntegerField(null=True)

    def from_json(self, val):
        self.BSNS_MBY_NM = val['BSNS_MBY_NM']
        self.CNTRCT_CNCLS_BGNDE = val['CNTRCT_CNCLS_BGNDE']
        self.CNTRCT_CNCLS_ENDDE = val['CNTRCT_CNCLS_ENDDE']
        self.HMPG_ADRES = val['HMPG_ADRES']
        self.HOUSE_DTL_SECD = val['HOUSE_DTL_SECD']
        self.HOUSE_DTL_SECD_NM = val['HOUSE_DTL_SECD_NM']
        self.HOUSE_MANAGE_NO = val['HOUSE_MANAGE_NO']
        self.HOUSE_NM = val['HOUSE_NM']
        self.HOUSE_SECD = val['HOUSE_SECD']
        self.HOUSE_SECD_NM = val['HOUSE_SECD_NM']
        self.HSSPLY_ADRES = val['HSSPLY_ADRES']
        self.HSSPLY_ZIP = val['HSSPLY_ZIP']
        self.MDHS_TELNO = val['MDHS_TELNO']
        self.MVN_PREARNGE_YM = val['MVN_PREARNGE_YM']
        self.PBLANC_NO = val['PBLANC_NO']
        self.PRZWNER_PRESNATN_DE = val['PRZWNER_PRESNATN_DE']
        self.RCRIT_PBLANC_DE = val['RCRIT_PBLANC_DE']
        self.SEARCH_HOUSE_SECD = val['SEARCH_HOUSE_SECD']
        self.SUBSCRPT_RCEPT_BGNDE = val['SUBSCRPT_RCEPT_BGNDE']
        self.SUBSCRPT_RCEPT_ENDDE = val['SUBSCRPT_RCEPT_ENDDE']
        self.TOT_SUPLY_HSHLDCO = val['TOT_SUPLY_HSHLDCO']
        return self
