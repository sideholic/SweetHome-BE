from rest_framework import serializers
from .models import *


class InfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Info
        fields = ('title', 'body', 'answer')


class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = ('title',
                  'body',
                  'createdAt',
                  'updatedAt',
                  'isDelete')


class AptSerializer(serializers.ModelSerializer):
    class Meta:
        model = Apt
        fields = (
            'BSNS_MBY_NM',
            'CNSTRCT_ENTRPS_NM',
            'CNTRCT_CNCLS_BGNDE',
            'CNTRCT_CNCLS_ENDDE',
            'GNRL_RNK1_CRSPAREA_RCEPT_PD',
            'GNRL_RNK1_ETC_AREA_RCPTDE_PD',
            'GNRL_RNK1_ETC_GG_RCPTDE_PD',
            'GNRL_RNK2_CRSPAREA_RCEPT_PD',
            'GNRL_RNK2_ETC_AREA_RCPTDE_PD',
            'GNRL_RNK2_ETC_GG_RCPTDE_PD',
            'HMPG_ADRES',
            'HOUSE_DTL_SECD',
            'HOUSE_DTL_SECD_NM',
            'HOUSE_MANAGE_NO',
            'HOUSE_NM',
            'HOUSE_SECD',
            'HOUSE_SECD_NM',
            'HSSPLY_ADRES',
            'HSSPLY_ZIP',
            'IMPRMN_BSNS_AT',
            'LRSCL_BLDLND_AT',
            'MDAT_TRGET_AREA_SECD',
            'MDHS_TELNO',
            'MVN_PREARNGE_YM',
            'NPLN_PRVOPR_PUBLIC_HOUSE_AT',
            'PARCPRC_ULS_AT',
            'PBLANC_NO',
            'PRZWNER_PRESNATN_DE',
            'PUBLIC_HOUSE_EARTH_AT',
            'RCEPT_BGNDE',
            'RCEPT_ENDDE',
            'RCRIT_PBLANC_DE',
            'RENT_SECD',
            'RENT_SECD_NM',
            'SPECLT_RDN_EARTH_AT',
            'SPSPLY_RCEPT_BGNDE',
            'SPSPLY_RCEPT_ENDDE',
            'SUBSCRPT_AREA_CODE',
            'SUBSCRPT_AREA_CODE_NM',
            'TOT_SUPLY_HSHLDCO',
        )


class UrbtySerializer(serializers.ModelSerializer):
    class Meta:
        model = Urbty
        fields = (
            'BSNS_MBY_NM',
            'CNTRCT_CNCLS_BGNDE',
            'CNTRCT_CNCLS_ENDDE',
            'HMPG_ADRES',
            'HOUSE_DTL_SECD',
            'HOUSE_DTL_SECD_NM',
            'HOUSE_MANAGE_NO',
            'HOUSE_NM',
            'HOUSE_SECD',
            'HOUSE_SECD_NM',
            'HSSPLY_ADRES',
            'HSSPLY_ZIP',
            'MDHS_TELNO',
            'MVN_PREARNGE_YM',
            'PBLANC_NO',
            'PRZWNER_PRESNATN_DE',
            'RCRIT_PBLANC_DE',
            'SEARCH_HOUSE_SECD',
            'SUBSCRPT_RCEPT_BGNDE',
            'SUBSCRPT_RCEPT_ENDDE',
            'TOT_SUPLY_HSHLDCO',
        )


class RemndrSerializer(serializers.ModelSerializer):
    class Meta:
        model = Remndr
        fields = (
            'HOUSE_MANAGE_NO',
            'PBLANC_NO',
            'HOUSE_NM',
            'HOUSE_SECD',
            'HOUSE_SECD_NM',
            'HSSPLY_ZIP',
            'HSSPLY_ADRES',
            'TOT_SUPLY_HSHLDCO',
            'RCRIT_PBLANC_DE',
            'SUBSCRPT_RCEPT_BGNDE',
            'SUBSCRPT_RCEPT_ENDDE',
            'SPSPLY_RCEPT_BGNDE',
            'SPSPLY_RCEPT_ENDDE',
            'GNRL_RCEPT_BGNDE',
            'GNRL_RCEPT_ENDDE',
            'PRZWNER_PRESNATN_DE',
            'CNTRCT_CNCLS_BGNDE',
            'CNTRCT_CNCLS_ENDDE',
            'HMPG_ADRES',
            'BSNS_MBY_NM',
            'MDHS_TELNO',
            'MVN_PREARNGE_YM'
        )


class AptDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = AptDetail
        fields = (
            'HOUSE_MANAGE_NO',
            'PBLANC_NO',
            'MODEL_NO',
            'HOUSE_TY',
            'SUPLY_AR',
            'SUPLY_HSHLDCO',
            'SPSPLY_HSHLDCO',
            'MNYCH_HSHLDCO',
            'NWWDS_HSHLDCO',
            'LFE_FRST_HSHLDCO',
            'OLD_PARNTS_SUPORT_HSHLDCO',
            'INSTT_RECOMEND_HSHLDCO',
            'ETC_HSHLDCO',
            'TRANSR_INSTT_ENFSN_HSHLDCO',
            'LTTOT_TOP_AMOUNT',
        )


class UrbtyDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = UrbtyDetail
        fields = (
            'PBLANC_NO',
            'HOUSE_MANAGE_NO',
            'MODEL_NO',
            'GP',
            'TP',
            'SUPLY_AR',
            'SUPLY_HSHLDCO',
            'SUPLY_AMOUNT',
            'SUBSCRPT_REQST_AMOUNT',
        )


class RemndrDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = RemndrDetail
        fields = (
            'HOUSE_MANAGE_NO',
            'PBLANC_NO',
            'MODEL_NO',
            'HOUSE_TY',
            'SUPLY_AR',
            'SUPLY_HSHLDCO',
            'SPSPLY_HSHLDCO',
            'LTTOT_TOP_AMOUNT',
        )
