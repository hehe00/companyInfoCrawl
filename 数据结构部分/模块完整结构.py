#coding=utf-8
#1股东信息

LEGINFO =  {
    "ID": "",        #唯一标示
    "BLICNO": "",    #证照编号
    "BLICTYPE": "",  #证照类型
    "INV": "",   #主管部门名称/股东/发起人名称
    "INVTYPE": "",   #主管部门类型/股东/发起人类型
    "INVDETAIL": {
        "INV": "",    #主管部门名称/股东/发起人名称
        "LISUBCONAM": "",  #累计认缴额
        "LIACCONAM": "",   #累计实缴额
        "PUBDATE": "",     #公示日期
        "CZRATIO": "",     #出资比例
        "PAYINFO": [
           {"CONFORM": "",    #认缴出资方式
            "SUBCONAM": "",   #认缴出资额
            "CONDATE": ""}   #认缴出资日期
        ],
        "REALPAYINFO":[
           {"CONFORM": "",    #实缴出资方式
            "ACCONAM": "",    #实缴出资额
            "CONDATE": ""}   #实缴出资日期
        ]
    }
}

#2主要人员信息_
PERINFO = {
    "NAME": "",       #姓名
    "POSITION": ""    #职位
}

#3分支机构_
BRANINFO =  {
    "BRNAME": "",     #名称
    "LEREP": "",      #法定代表人
    "REGSTATE": "",   #登记状态
    "ESTDATE": "",    #成立日期
    "REGNO": "",      #注册号
    "REGORG": "",     #登记机关
    "UNISCID": "",    #统一社会信用代码
    "TEL": "",        #联系电话
    "ADDR": "",       #通信地址
    "DOM": ""         #住所
}

#4变更信息_
CHGINFO = {
    "ALTITEM": "",    #变更事项
    "ALTDATE": "",    #变更日期
    "ALTBE": "",      #变更前内容
    "ALTAF": ""       #变更后内容
}

#5经营异常_
EXCEINFO = {
    "SPECAUSE": "",   #列入经营异常名录原因
    "ABNTIME": "",    #列入日期
    "REMEXCPRES": "", #移出经营异常名录
    "REMDATE": "",    #移出日期
    "DECORG": "",     #作出决定机关
    "YCCAUSE": "",    #移除原因
    "YCORG": ""       #移除机关
}

#6股权出质_
EQUINFO = {
    "EQUPLEDATE": "",     #股权出质登记日期
    "EQUITYNO": "",       #股权登记编号
    "TYPE": "",           #状态
    "IMPAM": "",          #出质股权数额
    "REGCAPCUR": "",      #出质股权数额币种
    "PLEDAMUNIT": "",     #出质股权数额单位
    "PLEDGOR": "",        #出质人
    "PLEDNO": "",         #出质人证照号码（添加）
    "IMPORG": "",         #质权人
    "BLICNO": "",         #质权人证照号码
    "BLICTYPE": "",       #质权人证照类型
    "REMARK": ""          #备注
}

#7商标信息
TMINFO = {
    "APP_DATE": "",       #申请日期
    "TM_LOGO": "",        #商标
    "TM_NAME": "",        #商标名称
    "REGNO": "",          #注册号
    "TYPE": "",           #类别
    "STATUS": ""          #状态
}

#8专利信息
PATENT = {
    "APP_PUB_NUM": "",       #申请公布号
    "APP_NO": "",            #申请号
    "CLSFYNO": "",           #分类号
    "IMG_URL": "",           #图片地址
    "PATENT_NAME": "",       #专利/发明名称
    "ADDRESS": "",           #地址
    "INVENTOR": "",          #发明人
    "APPLICANT_NAME": "",    #申请人
    "APP_DATE": "",          #申请日期
    "APP_PUB_DATE": "",      #申请公布日
    "AGENCY": "",            #代理机构
    "AGENT": "",             #代理人
    "ABSTRACTS": ""          #摘要
}

#9著作权
COPYRIGHT = {
    "REGTIME": "",            #批准日期/登记日期
    "FULLNAME": "",           #软件全称
    "NAME": "",               #软件简称
    "REGNUM": "",             #登记号
    "CATNUM": "",             #分类号
    "VERSION": "",            #版本号
    "AUTHOR_NATIONALITY": "", #著作权人(国籍)"
    "PUBLISHTIME": ""         #首次发表日期
}

#10股权冻结信息
FREEZEINFO = {
    "BEEXECUTED": "",     #被执行人
    "EXECUTEDAM": "",     #股权数额
    "COURTDEPT": "",      #执行法院
    "REFERENCENUM": "",   #协助公示通知书文号
    "PUBDATE": "",        #公示日期
    "FREEZEFROM": "",     #冻结期限自
    "FREEZETO": ""        #冻结期限至
}

#11对外投资
INVEST = {
    "EXT_COMPANY_NAME": "",  #被投资企业名称
    "EXT_LEREP": "",         #被投资企业法人
    "CAPITAL": "",           #注册资本
    "AMOUNT": "",            #投资数额
    "RATIO": "",             #投资比例
    "REGDATE": "",           #注册时间
    "STATUS": ""             #状态
}

#12严重违法
LAWINFO = {
    "SERILLREA": "",  #列入严重违法企业名单原因
    "ABNTIME": "",    #列入日期
    "REMDATE": "",    #移出日期
    "REMEXCPRES": "", #移出严重违法企业名单原因
    "DECORG": ""     #作出决定机关
}


#13产品信息
productInfo = {
    "rowkeySource": "", #rowkey来源
    "rowkey": "", #md5
    "classes" : "",      #领域
    "filterName" : "",   #产品简称
    "icon" : "",         #图标
    "type" : "",         #产品分类
    "brief" : "",        #描述
    "name" : ""         #产品名称
}

#14债券信息
bondInfo = {
    "rowkeySource": "", #rowkey来源
    "rowkey": "", #md5
    "bondName": "", #债券名称
    "bondNum": "", #债券代码
    "publisherName": "", #发行人
    "bondType": "", #债券类型
    "publishExpireTime": "", #债劵到期日
    "publishTime": "", #债劵发行日
    "bondTimeLimit": "", #债劵期限
    "ssjyr" : "", #上市交易日
    "calInterestType": "", #计息方式
    "bondStopTime": "", #债劵摘牌日
    "xxpjjg" : "",  #信用评级机构
    "debtRating": "", #债项评级
    "faceValue": "", #面值
    "ccll" : "", #参考利率
    "pmll" : "", #票面利率
    "realIssuedQuantity": "", #实际发行量(亿)
    "planIssuedQuantity": "", #计划发行量(亿)
    "issuedPrice": "",  #发行价格(元)
    "lc" : "",  #利差（BP）
    "payInterestHZ": "",  #付息频率
    "startCalInterestTime": "", #债券起息日
    "exeRightType": "",  #行权类型
    "xqrq" : "",  #行权日期
    "createTime": "", #发行日期
    "escrowAgent": "", #托管机构
    "flowRange": ""  #流通范围
}


#15企业关系
companyRelationship = {
    "rowkeySource": "", #rowkey来源
    "rowkey": "", #md5
    "result": "" #json串"
}

#16高管信息
seniorPeople = {
    "rowkeySource": "", #rowkey来源
    "rowkey": "", #md5
    "position": "", #职务
    "sex": "", #性别
    "education": "", #学历
    "resume": "", #简介
    "term": "", #本届任期
    "name": "", #姓名
    "age": "", #年龄
    "reportDate": "", #公告日期
    "salary": "", #薪酬
    "numberOfShares": "" #持股数"
}

#17网站备案
websiteRecode = {
    "rowkeySource": "", #rowkey来源
    "rowkey": "", #md5
    "examineDate" : "", #检查时间
    "webName" : "", #网站名称
    "webSite" : "", #网站首页
    "ym" : "", #域名
    "bah" : "", #备案号
    "status" : "", #状态
    "companyType" : "" #公司类型
}

#18抽查检查
spotCheck = {
    "rowkeySource": "", #rowkey来源
    "rowkey": "", #md5
    "checkType" : "", #类型
    "checkResult" : "", #结果
    "checkOrg" : "", #检查实施机关
    "checkDate" : "" #日期"
}

#19进出口信用
impExpCredit = {
    "rowkeySource": "", #rowkey来源
    "rowkey": "", #md5
    "xydj":[
        {
        "creditRating" : "", #信用等级
        "authenticationCode" : "", #认证证书编码
        "identificationTime" : "" #认定时间"
        }
    ],
    "xzcf": [
        {
            "penaltyDate" : "", #处罚日期
            "natureOfCase" : "", #案件性质
            "decisionNumber" : "", #行政处罚决定书编号
            "party" : "" #当事人"
        }
    ],
    "zcxx":
        {
            "industryCategory" : "", #行业种类
            "validityDate" : "", #报关有效期
            "annualReport" : "", #年报情况
            "economicDivision" : "", #经济区划
            "status" : "", #海关注销标识
            "recordDate" : "", #注册日期
            "managementCategory" : "", #经营类别
            "administrativeDivision" : "", #行政区划
            "crCode" : "", #海关注册号
            "specialTradeArea" : "", #特殊贸易区域
            "customsRegisteredAddress" : "", #注册海关
            "types" : "" #跨境贸易电子商务类型"
        }
}

#20资质证书
qualificationCertificate = {
    "rowkeySource": "", #rowkey来源
    "rowkey": "", #md5
    "licenceType" : "", #证书类型
    "zsbh" : "", #证书编号
    "issueDate" : "", #发证日期
    "jzrq" : "", #截止日期
    "companyName" : "", #企业名称/申请人
    "bz" : "", #标准
    "ztbhsj" : "", #证书状态变化时间
    "reason" : "", #原因
    "scc" : "", #生产厂
    "scfzrq" : "", #首次发证日期
    "cpmc" : "", #产品名称
    "zzs" : "", #制造商
    "xinghao" : "", #型号/规格
    "xzt" : "", #现状态
    "ywzl" : "", #业务种类
    "xkzbh" : "", #许可证编号
    "ywfgfw" : "", #业务覆盖范围
    "toDate" : "", #有效期至
    "hm" : "", #号码
    "sydw" : "", #使用单位
    "pzyt" : "", #批准用途
    "deviceName" : "", #设备名称
    "deviceType" : "", #设备型号
    "applyCompany" : "", #申请单位
    "productCompany" : "" #生产企业
}

#21税务评级|信用等级|守信红名单
taxRating = {
    "rowkeySource": "", #rowkey来源
    "rowkey": "", #md5
    "grade": "", #纳税等级|等级
    "year": "", #年份|评价年度
    "evalDepartment": "", #评价单位|所属分局
    "type": "", #0国税 1地税
    "idNumber": "", #纳税人识别号
    "name": "" #纳税人名称"
}

#22招投标
bidding = {
    "rowkeySource": "", #rowkey来源
    "rowkey": "", #md5
    "content" : "", #整个内容源码
    "title" : "", #标题
    "purchaser" : "", #采购人
    "abs" : "", #公告概要
    "publishTime" : "", #发布时间
    "proxy" : "", #公司名称
    "link" : "", #原始链接
    "intro" : "" #全部内容"  # 去掉源码中无用信息
}


#23税务登记及一般纳税人资格信息
taxRegist = {
    "rowkeySource": "", #rowkey来源
    "rowkey": "", #md5
    "nsrsbh" : "", #纳税人识别号
    "nszg" : "", #纳税资格名称
    "fddbr" : "", #法定代表人
    "dz" : "", #地址
    "yxqq" : "", #有效期起
    "zryxqz" : "", #暂认有效期止
    "ssswjg" : "", #所属税务机关
    "yxqz" : "", #有效期止
    "djzclx" : "", #登记注册类型
    "jyfw" : "", #经营范围
    "pzsljg" : "", #批准设立机关
    "kjyw" : "", #扣缴义务
    "fzrq" : "", #发证日期
    "nsrzt" : "", #纳税人状态
    "nsrlb" : "" #增值税纳税人类别"
}

#24失踪纳税人公告
missNotice = {
    "rowkeySource": "", #rowkey来源
    "rowkey": "", #md5
    "nsrsbh" : "", #纳税人识别号
    "fddbr" : "", #法定代表人
    "scjydz" : "", #生产经营地址
    "swjg" : "", #税务机关名称
    "zjlx" : "", #证件类型
    "fddbrzjhm" : "", #法定代表人证件号码
    "zclx" : "", #登记注册类型：
    "rjrq" : "" #认定日期"
}

#25非正常户
impRoper = {
    "rowkeySource": "", #rowkey来源
    "rowkey": "", #md5
    "zggsjg" : "", #主管国税机关
    "nsrsbh" : "", #纳税人识别号
    "fddbr" : "", #法定代表人
    "zjlx" : "", #证件类型
    "fddbrsfzhm" : "", #法定代表人身份证号码
    "scjydz" : "", #生产经营地址
    "rdrq" : "", #非正常认定日期
    "fbrq":"", #发布日期
    "zclx" : "", #注册类型
    "zzjgdm" : "", #组织机构代码
    "qsbz" : "", #欠税币种
    "qssz" : "", #欠税税种
    "xqsje" : "", #当前新发生的欠税金额
    "kprq" : "", #开票日期
    "jkrq" : "", #缴款期限
    "qsje" : "", #欠税金额
    "sxrq":"", #证件失效确认日期
    "beizhu" : "" #备注"
}

#26 失信公告 
dishonestyNotice = {
    "rowkeySource": "", #rowkey来源
    "rowkey": "", #md5
    "frfzr": "", #法定代表人或者负责人姓名
    "age": "", #年龄
    "sex": "", #性别
    "body": "", #全部内容
    "lxqk": "", #被执行人的履行情况
    "yiwu": "", #生效法律文书确定的义务
    "court": "", #执行法院
    "yjdw": "", #做出执行依据单位
    "sortTime": "", #立案时间时间戳
    "province": "", #省份
    "sortTimeString": "", #立案时间
    "jtqx": "", #失信被执行人行为具体情形
    "pname": "", #被执行人姓名/名称
    "postTime": "", #发布时间
    "yjCode": "", #执行依据文号
    "sxggId": "", #法海自定义id
    "caseNo": "", #案号
    "idcardNo": "", #身份证号码/组织机构代码
    "ylx": "", #已履行部分
    "wlx": "", #未履行部分
    "datafrom": "", #数据来源
    "dataType": "" #sxgg"
}

#27行政许可
administrativeLicensing = {
    "rowkeySource": "", #rowkey来源
    "rowkey": "", #md5
    "xkjdwsh" : "", #行政许可决定文书号
    "splx" : "", #审批类别/类型
    "frdb" : "", #法定代表人姓名、法人姓名
    "nrxk" : "", #许可内容
    "xkyxq": "", #许可有效期
    "xkjzq" : "", #许可截止期
    "dfbm" : "", #地方编码
    "xkjg" : "", #许可机关
    "xmmc" : "", #项目名称
    "tyshxydm" : "", #统一社会信用代码
    "zzjgdm" : "", #组织机构代码
    "nsrsbh" : "", #纳税人识别号
    "gsdjm" : "", #工商登记码
    "sedjh" : "", #税务登记号
    "wspzxh": "", #文书凭证序号
    "frzjhm" : "", #法人证件号码
    "xkjdrq" : "", #许可决定日期
    "xkzt" : "", #许可状态、当前状态
    "sjgxsj" : "", #数据更新时间
    "beizhu" : "", #备注
    "shrq" : "" #审核日期"
}


#28重大税收违法
taxContrave = {
    "rowkeySource": "", #rowkey来源
    "rowkey": "", #md5
    "sjly": "", #数据来源
    "sjlx": "", #数据类别
    "nsrmc" : "", #纳税人名称
    "nsrsbh": "", #纳税人识别码
    "zzjgdm" : "", #组织机构代码
    "dz": "", #注册地址
    "frxm" : "", #法定代表人或者负责人姓名
    "frxb" : "", #法定代表人或者负责人性别
    "frzjmc" : "", #法定代表人或者负责人证件名称
    "cwfzrxm" : "", #负有直接责任的财务负责人姓名
    "cwfzrxb" : "", #负有直接责任的财务负责人性别
    "cwfzrzjmc" : "", #负有直接责任的财务负责人证件名称
    "zjjg" : "", #负有直接责任的中介机构信息及其从业人员信息
    "ajxz" : "", #案件性质
    "wfss" : "", #主要违法事实", #两个都赋值
    "yjcfqk" : "", #相关法律依据及税务处理处罚情况", #两个都赋值
    "sbrq" : "", #案件上报期
    "zxgxrq" : "", #最新更新日期
    "zrrxm" : "", #自然人姓名
    "zrrxb" : "", #自然人性别
    "fzrzjhm" : "", #法定代表人或者负责人证件号码
    "fzrxx" : "", #法定代表人或者负责人姓名、性别、证件名称及号码（负责人信息）
    "zjcwfzrzjhm" : "", #负有直接责任的财务负责人证件号码
    "zjcwfzrxx" : "", #负有直接责任的财务负责人姓名、性别、证件名称及号码(直接财务负责人信息)
    "sjfzrxx": "" #实际负责人姓名、性别及身份证号码（或其他证件号码）(实际负责人信息)"
}

#29 政府采购严重违法失信信息
purchaseIllegal = {
    "rowkeySource": "", #rowkey来源
    "rowkey": "", #md5
    "sjly": "", #数据来源
    "sjlx": "", #数据类别
    "gysmc": "", #供应商或代理机构名称
    "dz": "", #地址
    "jtqx": "", #不良行为的具体情形
    "cfjg": "", #处罚结果
    "cfyj": "", #处罚依据
    "cfrq": "", #处罚（记录）日期
    "zfdw": "", #执法（记录）单位
    "cfjssj": "", #处罚结束时间
    "zxgxrq": "" #最新更新日期"
}

#30 行政处罚
administrativePenalty = {
    "rowkeySource": "", #rowkey来源
    "rowkey": "", #md5
    "jdwsh" : "", #行政处罚决定文书号
    "wfxwlx": "", #违法行为类型
    "cfzl": "", #处罚种类
    "fkje": "", #罚款金额
    "msje": "", #没收金额
    "jddwmc" : "", #作出行政处罚决定单位名称|作出处罚决定的机关名称|督办单位
    "zcxzcfjdrq" : "", #作出行政处罚决定日期
    "fddbr" : "", #法定代表人|概述（信用中国里，概述为法定代表人-唐山达丰焦化有限公司）
    "bz": "", #备注
    "zywfss" : "", #主要违法事实|环境违法事实和依据
    "tyshxydm" : "", #统一社会信用代码
    "nsrsbh": "", #纳税人识别号
    "anmc" : "", #案件名称
    "zrrmc" : "", #自然人或个体工商户名称|单位名称
    "zjlx" : "", #证件类型
    "frzjhm" : "", #法人证件号码
    "cflb1": "", #处罚类别1
    "cflb2": "", #处罚类别2
    "cfsy" : "", #处罚事由
    "cfyjjg" : "", #处罚依据、处罚结果
    "cfyj": "", #处罚依据|行政处罚的种类和依据
    "cfjg": "", #处罚结果
    "zzjgdm" : "", #组织机构代码|单位的组织机构编码
    "gsdjm" : "", #工商登记码
    "swdjh" : "", #税务登记号
    "xzxdr" : "", #行政相对人名称
    "wfdjrq" : "", #违法行为登记日期
    "cfjdszzrq" : "", #处罚决定书制作日期
    "cfsxq" : "", #处罚生效期
    "cfjzq" : "", #处罚截止期
    "dqzt" : "", #当前状态
    "dqclzt": "", #当前处理状态
    "dfbm": "", #地方编码
    "gsqx": "", #公示期限
    "nsrzt": "", #纳税人状态
    "gxsj": "" #更新时间|最新更新日期"
}

#31 欠税公告
owingTaxesNotice = {
    "rowkeySource": "", #rowkey来源
    "rowkey": "", #md5
    "fbrq": "", #发布日期
    "narsbh" : "", #纳税人识别号
    "qssz" : "", #欠税税种
    "qsbe" : "", #欠税币额
    "dqxfsqsye" : "", #当前新发生的欠税余额
    "swjgmc" : "", #税务机关名称
    "jydd" : "", #经营地点
    "nsrlx" : "", #纳税人类型
    "fzrxm" : "", #负责人姓名 （法定代表人）
    "sfzjzl" : "", #身份证件种类
    "zjhm" : "", #证件号码
    "rdrq" : "", #认定日期
    "xqbz" : "", #新欠币种
    "qsssq" : "", #欠税所属期
    "sjly": "" #数据来源"
}

#32 动产抵押
chattelMortgage = {
    "dcdydjbh":"",          #动产抵押登记编号
    "djrq":"",              #登记日期
    "djjg":"",              #登记机关
    "zt":"",                #状态
    "bdbzqzl":"",           #被担保债权种类
    "bdbzqse":"",           #被担保债权数额
    "bdbzqbz":"",           #被担保债权数额币种
    "zwrlxzwqxks":"",       #债务人履行债务的期限自
    "zwrlxzwqxjs":"",       #债务人履行债务的期限至
    "dbfw":"",              #担保范围
    "bz":"",                #备注
    "dcdy_bgxx":[],         #动产抵押变更信息
    "dyw":[{                #抵押物
        "dywmc":"",         #抵押物名称
        "syqgs":"",         #所有权或使用权归属
        "gsqk":"",          #数量、质量、状况、所在地等情况
        "dywbz":""          #(抵押物)备注
    }],                        
    "dyqrgk":[{             #抵押权人概况
        "dyqrmc":"",        #抵押权人名称
        "dyqrzz":"",        #抵押权人证照／证件类型
        "zzhm":"",          #证件／证照号码
        "zsd":""            #住所地
    }]           
}

#33 招聘信息
employments = {
    "title":"",             #招聘职称
    "city":"",              #所在城市
    "district":"",          #所在区
    "companyName":"",       #公司名字
    "oriSalary":"",         #薪资
    "urlPath":"",           #外网链接
    "startdate":"",         #招聘开始日期
    "enddate":"",           #招聘截止日期
    "source":"",            #来源
    "education":"",         #教育水平
    "employerNumber":"",    #招聘人数
    "experience":"",        #经验
    "description":"",       #职位描述
    "createTime":"",        #创建时间
    "updateTime":"",        #更新时间
    "id":""                 #对应表id
}

