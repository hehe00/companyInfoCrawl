#coding=utf-8

#企业信息
companyInformation = {
    #01 LEGINFO                     股东信息        
    #02 PERINFO                     主要人员信息    
    #03 BRANINFO                    分支机构        
    #04 CHGINFO                     变更信息        
    #05 EXCEINFO                    经营异常        
    #06 EQUINFO                     股权出质        
    #07 TMINFO                      商标信息        
    #08 PATENT                      专利            
    #09 COPYRIGHT                   著作权      
    #10 FREEZEINFO                  股权冻结信息    
    #11 INVEST                      对外投资        
    #12 LAWINFO                     严重违法  

    #13 productInfo                 产品信息        
    #14 bondInfo                    债券信息      
    #15 companyRelationship         企业关系        
    #16 seniorPeople                高管信息        
    #17 websiteRecode               网站备案        
    #18 spotCheck                   抽查检查        
    #19 impExpCredit                进出口信用 
    #20 qualificationCertificate    资质证书    
    #21 taxRating                   税务评级|信用等级|守信红名单        
    #22 bidding                     招投标       
    #23 taxRegist                   税务登记及一般纳税人资格信息    
    #24 missNotice                  失踪纳税人公告                  
    #25 impRoper                    非正常户   
    #26 dishonestyNotice            失信公告                        
    #27 administrativeLicensing     行政许可
    #28 taxContrave                 重大税收违法                    
    #29 purchaseIllegal             政府采购严重违法失信信息

    #30 administrativePenalty       行政处罚
    #31 owingTaxesNotice            欠税公告 
    #32 chattelMortgage             动产抵押
    #33 employments                 招聘信息
    
    #34 equityRatio              股权结构图
    #35 investtree               投资族谱
    #36 roles                    人所有角色
    #37 findHistoryRongzi        融资历史
    #38 findTzanli               投资事件
    #39 annualreport             年报
    #40 yuqing                   舆情
    #41 companyTag               企业标签（高新）
    #42 baiduIdx                 百度相关条数
    #43 rptPubDate               年报更新时间


    LEGINFO                 ={"operation":"replace", "data_type":"gs_V1", "data": []}
    PERINFO                 ={"operation":"replace", "data_type":"gs_V1", "data": []}
    BRANINFO                ={"operation":"append",  "data_type":"gs_V1", "data": []}
    CHGINFO                 ={"operation":"append",  "data_type":"gs_V1", "data": []}
    EXCEINFO                ={"operation":"append",  "data_type":"gs_V1", "data": []}
    EQUINFO                 ={"operation":"append",  "data_type":"gs_V1", "data": []}
    TMINFO                  ={"operation":"append",  "data_type":"gs_V1", "data": []}
    PATENT                  ={"operation":"append",  "data_type":"gs_V1", "data": []}
    COPYRIGHT               ={"operation":"append",  "data_type":"gs_V1", "data": []}
    FREEZEINFO              ={"operation":"append",  "data_type":"gs_V1", "data": []}
    INVEST                  ={"operation":"append",  "data_type":"gs_V1", "data": []}
    LAWINFO                 ={"operation":"append",  "data_type":"gs_V1", "data": []}

    productInfo             ={"operation":"append",  "data_type":"gs",    "data": []}
    bondInfo                ={"operation":"append",  "data_type":"gs",    "data": []}
    companyRelationship     ={"operation":"replace", "data_type":"gs",    "data": []}
    seniorPeople            ={"operation":"replace", "data_type":"gs",    "data": []}
    websiteRecode           ={"operation":"append",  "data_type":"gs",    "data": []}
    spotCheck               ={"operation":"append",  "data_type":"gs",    "data": []}
    qualificationCertificate={"operation":"append",  "data_type":"gs",    "data": []}
    impExpCredit            ={"operation":"append",  "data_type":"gs",    "data": []}
    administrativeLicensing = {"operation":"append", "data_type":"gs",    "data": []}
    administrativePenalty   ={"operation":"append",  "data_type":"gs",    "data": []}

    taxRating               ={"operation":"append",  "data_type":"sw",    "data": []}
    taxContrave             ={"operation":"append",  "data_type":"sw",    "data": []}
    missNotice              ={"operation":"append",  "data_type":"sw",    "data": []}
    taxRegist               ={"operation":"append",  "data_type":"sw",    "data": []}
    impRoper                ={"operation":"append",  "data_type":"sw",    "data": []}
    owingTaxesNotice        ={"operation":"append",  "data_type":"gs/sw", "data": []}

    bidding                 ={"operation":"append",  "data_type":"cz",    "data": []}
    purchaseIllegal         ={"operation":"append",  "data_type":"cz",    "data": []}
    dishonestyNotice        ={"operation":"append",  "data_type":"sf",    "data": []}
    chattelMortgage         ={"operation":"append",  "data_type":"gs",    "data": []}
    employments             ={"operation":"append",  "data_type":"rs",    "data": []}  #rs 人事
    
    yuqing                  ={"operation":"append", "data_type":"gs", "data": []}   #舆情
    annualreport            ={"operation":"append", "data_type":"gs", "data": []}  #年报
    findTzanli              ={"operation":"append", "data_type":"gs", "data": []}  #投资事件
    findHistoryRongzi       ={"operation":"append", "data_type":"gs", "data": []}  #融资历史
    roles                   ={"operation":"replace", "data_type":"gs", "data": []}  #人所有角色
    investtree              ={"operation":"append", "data_type":"gs", "data": []}  #投资族谱
    equityRatio             ={"operation":"replace", "data_type":"gs", "data": []}  #股权结构图
    companyTag              ={"operation":"replace", "data_type":"gs", "data": []}  #企业标签（高新）
    

    #调整部分如下：
    '''
        @1 动产抵押  MORTINFO 调整为 chattelMortgage，     原结构不满足实际情况，抵押物和抵押权人概况调整为列表；
        @2 行政处罚  PUNINFO  调整为 administrativePenalty，向前兼容、新增字段；
        @3 欠税公告  TOWNTAX  调整为 owingTaxesNotice，原结构不满足实际情况，大小写统一；
        @4 重大税收违法 及 政府采购违法 模块名调整，字段新增；
    '''

}

