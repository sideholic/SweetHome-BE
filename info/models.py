import json

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


class Remndr(models.Model):
    HOUSE_MANAGE_NO = models.IntegerField(primary_key=True)
    PBLANC_NO = models.IntegerField()
    HOUSE_NM = models.TextField(null=True)
    HOUSE_SECD = models.TextField(null=True)
    HOUSE_SECD_NM = models.TextField(null=True)
    HSSPLY_ZIP = models.TextField(null=True)
    HSSPLY_ADRES = models.TextField(null=True)
    TOT_SUPLY_HSHLDCO = models.IntegerField()
    RCRIT_PBLANC_DE = models.TextField(null=True)
    SUBSCRPT_RCEPT_BGNDE = models.TextField(null=True)
    SUBSCRPT_RCEPT_ENDDE = models.TextField(null=True)
    SPSPLY_RCEPT_BGNDE = models.TextField(null=True)
    SPSPLY_RCEPT_ENDDE = models.TextField(null=True)
    GNRL_RCEPT_BGNDE = models.TextField(null=True)
    GNRL_RCEPT_ENDDE = models.TextField(null=True)
    PRZWNER_PRESNATN_DE = models.TextField(null=True)
    CNTRCT_CNCLS_BGNDE = models.TextField(null=True)
    CNTRCT_CNCLS_ENDDE = models.TextField(null=True)
    HMPG_ADRES = models.TextField(null=True)
    BSNS_MBY_NM = models.TextField(null=True)
    MDHS_TELNO = models.TextField(null=True)
    MVN_PREARNGE_YM = models.TextField(null=True)

    def from_json(self, val):
        self.HOUSE_MANAGE_NO = val['HOUSE_MANAGE_NO']
        self.PBLANC_NO = val['PBLANC_NO']
        self.HOUSE_NM = val['HOUSE_NM']
        self.HOUSE_SECD = val['HOUSE_SECD']
        self.HOUSE_SECD_NM = val['HOUSE_SECD_NM']
        self.HSSPLY_ZIP = val['HSSPLY_ZIP']
        self.HSSPLY_ADRES = val['HSSPLY_ADRES']
        self.TOT_SUPLY_HSHLDCO = val['TOT_SUPLY_HSHLDCO']
        self.RCRIT_PBLANC_DE = val['RCRIT_PBLANC_DE']
        self.SUBSCRPT_RCEPT_BGNDE = val['SUBSCRPT_RCEPT_BGNDE']
        self.SUBSCRPT_RCEPT_ENDDE = val['SUBSCRPT_RCEPT_ENDDE']
        self.SPSPLY_RCEPT_BGNDE = val['SPSPLY_RCEPT_BGNDE']
        self.SPSPLY_RCEPT_ENDDE = val['SPSPLY_RCEPT_ENDDE']
        self.GNRL_RCEPT_BGNDE = val['GNRL_RCEPT_BGNDE']
        self.GNRL_RCEPT_ENDDE = val['GNRL_RCEPT_ENDDE']
        self.PRZWNER_PRESNATN_DE = val['PRZWNER_PRESNATN_DE']
        self.CNTRCT_CNCLS_BGNDE = val['CNTRCT_CNCLS_BGNDE']
        self.CNTRCT_CNCLS_ENDDE = val['CNTRCT_CNCLS_ENDDE']
        self.HMPG_ADRES = val['HMPG_ADRES']
        self.BSNS_MBY_NM = val['BSNS_MBY_NM']
        self.MDHS_TELNO = val['MDHS_TELNO']
        self.MVN_PREARNGE_YM = val['MVN_PREARNGE_YM']
        return self


class AptDetail(models.Model):
    class Meta:
        unique_together = (('PBLANC_NO', 'MODEL_NO'),)

    def from_json(self, val):
        self.HOUSE_MANAGE_NO = val['HOUSE_MANAGE_NO']
        self.PBLANC_NO = val['PBLANC_NO']
        self.MODEL_NO = val['MODEL_NO']
        self.HOUSE_TY = val['HOUSE_TY']
        self.SUPLY_AR = val['SUPLY_AR']
        self.SUPLY_HSHLDCO = val['SUPLY_HSHLDCO']
        self.SPSPLY_HSHLDCO = val['SPSPLY_HSHLDCO']
        self.MNYCH_HSHLDCO = val['MNYCH_HSHLDCO']
        self.NWWDS_HSHLDCO = val['NWWDS_HSHLDCO']
        self.LFE_FRST_HSHLDCO = val['LFE_FRST_HSHLDCO']
        self.OLD_PARNTS_SUPORT_HSHLDCO = val['OLD_PARNTS_SUPORT_HSHLDCO']
        self.INSTT_RECOMEND_HSHLDCO = val['INSTT_RECOMEND_HSHLDCO']
        self.ETC_HSHLDCO = val['ETC_HSHLDCO']
        self.TRANSR_INSTT_ENFSN_HSHLDCO = val['TRANSR_INSTT_ENFSN_HSHLDCO']
        self.LTTOT_TOP_AMOUNT = val['LTTOT_TOP_AMOUNT']
        return self

    ID = models.IntegerField(primary_key=True)
    HOUSE_MANAGE_NO = models.IntegerField(null=True)
    PBLANC_NO = models.IntegerField()
    MODEL_NO = models.CharField(null=True, max_length=300)
    HOUSE_TY = models.CharField(null=True, max_length=300)
    SUPLY_AR = models.CharField(null=True, max_length=300)
    SUPLY_HSHLDCO = models.IntegerField(null=True)
    SPSPLY_HSHLDCO = models.IntegerField(null=True)
    MNYCH_HSHLDCO = models.IntegerField(null=True)
    NWWDS_HSHLDCO = models.IntegerField(null=True)
    LFE_FRST_HSHLDCO = models.IntegerField(null=True)
    OLD_PARNTS_SUPORT_HSHLDCO = models.IntegerField(null=True)
    INSTT_RECOMEND_HSHLDCO = models.IntegerField(null=True)
    ETC_HSHLDCO = models.IntegerField(null=True)
    TRANSR_INSTT_ENFSN_HSHLDCO = models.IntegerField(null=True)
    LTTOT_TOP_AMOUNT = models.CharField(null=True, max_length=300)

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__,
                          sort_keys=True, indent=4)


class UrbtyDetail(models.Model):
    class Meta:
        unique_together = (('PBLANC_NO', 'TP'),)

    def from_json(self, val):
        self.PBLANC_NO = val['PBLANC_NO']
        self.HOUSE_MANAGE_NO = val['HOUSE_MANAGE_NO']
        self.MODEL_NO = val['MODEL_NO']
        self.GP = val['GP']
        self.TP = val['TP']
        self.SUPLY_AR = val['SUPLY_AR']
        self.SUPLY_HSHLDCO = val['SUPLY_HSHLDCO']
        self.SUPLY_AMOUNT = val['SUPLY_AMOUNT']
        self.SUBSCRPT_REQST_AMOUNT = val['SUBSCRPT_REQST_AMOUNT']
        return self

    ID = models.IntegerField(primary_key=True)
    PBLANC_NO = models.IntegerField()
    HOUSE_MANAGE_NO = models.IntegerField(null=True)
    MODEL_NO = models.CharField(null=True, max_length=300)
    GP = models.CharField(null=True, max_length=300)
    TP = models.CharField(null=True, max_length=300)
    SUPLY_AR = models.CharField(null=True, max_length=300)
    SUPLY_HSHLDCO = models.IntegerField(null=True)
    SUPLY_AMOUNT = models.CharField(null=True, max_length=300)
    SUBSCRPT_REQST_AMOUNT = models.CharField(null=True, max_length=300)


class RemndrDetail(models.Model):
    class Meta:
        unique_together = (('PBLANC_NO', 'MODEL_NO'),)

    def from_json(self, val):
        self.HOUSE_MANAGE_NO = val['HOUSE_MANAGE_NO']
        self.PBLANC_NO = val['PBLANC_NO']
        self.MODEL_NO = val['MODEL_NO']
        self.HOUSE_TY = val['HOUSE_TY']
        self.SUPLY_AR = val['SUPLY_AR']
        self.SUPLY_HSHLDCO = val['SUPLY_HSHLDCO']
        self.SPSPLY_HSHLDCO = val['SPSPLY_HSHLDCO']
        self.LTTOT_TOP_AMOUNT = val['LTTOT_TOP_AMOUNT']
        return self

    ID = models.IntegerField(primary_key=True)
    HOUSE_MANAGE_NO = models.IntegerField(null=True)
    PBLANC_NO = models.IntegerField()
    MODEL_NO = models.CharField(null=True, max_length=300)
    HOUSE_TY = models.CharField(null=True, max_length=300)
    SUPLY_AR = models.CharField(null=True, max_length=300)
    SUPLY_HSHLDCO = models.IntegerField(null=True)
    SPSPLY_HSHLDCO = models.IntegerField(null=True)
    LTTOT_TOP_AMOUNT = models.CharField(null=True, max_length=300)
