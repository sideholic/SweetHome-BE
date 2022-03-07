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
