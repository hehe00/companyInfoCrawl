#信用等级
"ENTNAME" : "纳税人名称"
xydj:{
    "operation":"append",
    "data_type":"sw",
    "data":[{
        "rowkeySource" : "rowkey来源", #评价年度+纳税人识别号+纳税人名称
        "rowkey" : "md5",
        "grade" : "评定等级",
        "nsrmc" : "纳税人名称", 
        "nsrsbh" : "纳税人识别号/统一社会信用代码",
        "zgswgljg" : "主管税务管理机关",
        "pjnd" : "评价年度",  
        "province" : "省份",
        "city" : "城市",
        "fbjg": "发布机构",
        "fbsj": "发布时间 yyyy-mm-dd hh:mm:ss"}
        ]
    }

#欠税公告
"ENTNAME" : "纳税人名称"
qsgg:{
    "operation":"append",
    "data_type":"sw",
    "data":[{
        "rowkeySource":"rowkey来源", #非正常认定日期+纳税人识别号+纳税人名称+欠税币额/期末欠税余额+证件号码+当前新发生的欠税余额"
        "rowkey":"md5",
        "nsrmc" : "纳税人名称",
        "nsrlx" : "纳税人类型",    
        "nsrsbh" : "纳税人识别号",
        "fddbr" : "负责人姓名或法定代表人",
        "sfzjzl" : "身份证件种类",
        "zjhm" : "证件号码",
        "dom" : "经营地点",
        "qssz" : "欠税税种",
        "xqbz" : "新欠币种",
        "qsbe" : "欠税币额/期末欠税余额",
        "sqqsye": "上期欠税余额",
        "bqqjqs": "本期清缴欠税",
        "dqxfsdcsye" : "当前新发生的欠税余额",
        "swjgmc" : "税务机关名称",
        "fzcrdrq" : "非正常认定日期",
        "province" : "省份",
        "city" : " 城市",
        "qsssq":"欠税所属期",
        "bz":"备注",
        "fbjg":"发布机构"
        "fbsj":"发布时间"}
        ]
    }
 
#行政许可
"ENTNAME" : "纳税人名称"
xzxk:{
    "operation":"append",
    "data_type":"sw",
    "data":[{
        "rowkeySource":"rowkey来源",# 行政许可决定文书号+统一社会信用代码+纳税人识别号+纳税人名称
        "rowkey":"md5",
        "xmmc" : "项目名称",
        "xzxkjdwsh" : "行政许可决定文书号",
        "splb" : "审批类别  ",
        "xknr" : "许可内容",
        "nsrmc" : "行政相对人名称|纳税人名称",
        "tyshxydm" : "统一社会信用代码",
        "zzjgdm" : "组织机构代码",
        "nsrsbh" : "纳税人识别号",
        "gsdjh" : "工商登记码",
        "swdjh" : "税务登记号",
        "jmsfzh" : "居民身份证号,（和法人证件号码重复）"
        "fddbrxm" : "法定代表人姓名、法人姓名",
        "frzjhm" : "法人证件号码"
        "xkjdrq" : "许可决定日期",
        "xkjzq" : "许可截止期",
        "xkjg" : "许可机关",
        "xkzt" : "许可状态、当前状态",
        "dfbm" : "地方编码",
        "sjgxsj" : "数据更新时间",
        "bz" : "备注",
        "shrq" : "审核日期",
        "province" : "省份",
        "city" : "城市",
        "fbjg": "发布机构"
        "fbsj":"发布时间"
        "fingerPrint":"指纹 //用于主键存储，去除重复记录"}
        ]
    }

# 税务登记及一般纳税人资格信息
"ENTNAME" : "纳税人名称"
swdj_ybnsrzg:{
    "operation":"append",
    "data_type":"sw",
    "data":[{
        "rowkeySource":"rowkey来源",
        "rowkey":"md5",
         "nsrsbh" : "纳税人识别号",
        "nszgmc" : "纳税资格名称",
        "yxqq" : "有效期起",
        "zryxqz" : "暂认有效期止",
        "ssswjg" : "所属税务机关",
        "yxqz" : "有效期止",
        "nsrxm" : "纳税人姓名",
        "fddbr" : "法定代表人",
        "dom" : "地址",
        "djzclx" : "登记注册类型",
        "jyfw" : "经营范围",
        "pzsljg" : "批准设立机关",
        "kjyw" : "扣缴义务",
        "fzrq" : "发证日期",
        "nsrzt" : "纳税人状态",
        "zznsrlb" : "增值税纳税人类别",
        "province" : "省份",
        "city" : "城市",
        "fbjg":"发布机构",
        "fbsj":"发布时间",
        "nsrzglx":"纳税人资格类型",}
        ]
    }

    
# 重大税收违法
"ENTNAME" : "纳税人名称"
zdsswf:{
    "operation":"append",
    "data_type":"sw",
    "data":[{
        "rowkeySource":"rowkey来源",# 纳税人识别号+纳税人名称+案件性质+主要违法事实"
        "rowkey":"md5",        
        "nsrmc" : "纳税人名称",
        "nsrsbh" : "纳税人识别码",
        "zzjgdm" : "组织机构代码",
        "dom" : "注册地址",
        "fddbr" : "法定代表人或者负责人姓名",
        "fddbrxb" : "法定代表人或者负责人性别",
        "fddbrzjlx" : "法定代表人或者负责人证件类型",
        "fddbrzjhm":"法定代表人或者负责人证件号码"
        "fyzjzrdcwfzrxm" : "负有直接责任的财务负责人姓名",
        "fyzjzrdcwfzrxb" : "负有直接责任的财务负责人性别",
        "fyzjzrdcwfzrzjlx" : "负有直接责任的财务负责人证件类型",
        "fyzjzrdcwfzrzjhm":"负有直接责任的财务负责人证件号码",
        "fyzjzrdzjjgxxjqcyryxx" : "负有直接责任的中介机构信息及其从业人员信息",
        "ajxz" : "案件性质",
        "zywfss" : "主要违法事实",
        "xgflyjjswclcfqk" : "相关法律依据及税务处理处罚情况",
        "ajsbrq" : "案件上报期",
        "zxgxrq" : "最新更新日期",
        "province" : "省份",
        "city" : "城市",
        "fbjg":"发布机构"
        "fbsj":"发布时间"
        "fingerPrint":"指纹 //用于主键存储，去除重复记录"}
        ]
    }

#失踪纳税人公告
"ENTNAME" : "纳税人名称"
sznsrgg:{
    "operation":"append",
    "data_type":"sw",
    "data":[{
        "rowkeySource":"rowkey来源",
        "rowkey":"md5",
        "swjgmc" : "税务机关名称",
        "nsrsbh" : "纳税人识别号",
        "nsrmc" : "纳税人名称",
        "fddbr" : "法定代表人",
        "fddbrzjlx":"法定代表人证件类型",
        "fddbrzjhm" : "法定代表人证件号码",
        "djzclx" : "登记注册类型：",
        "dom" : "生产经营地址",
        "rdrq" : "认定日期",
        "province" : "省份",
        "city" : "城市",
        "fbjg":"发布机构"
        "fbsj":"发布时间",
        "fingerprint":"指纹 //用于主键存储，去除重复记录"}
        ]
    }

#行政处罚
"ENTNAME" : "纳税人名称"
xzcf:{
    "operation":"append",
    "data_type":"sw",
    "data":[{
        "rowkeySource":"rowkey来源", # 行政处罚决定文书号+统一社会信用代码+案件名称+法定代表人"
        "rowkey":"md5",
        "xzcfjdwsh" : "行政处罚决定文书号",
        "ajmc" : "案件名称",
        "zrrhgtgshmc" : "自然人或个体工商户名称",
        "frhqtzzmc" : "法人或其他组织名称",
        "fddbr" : "法定代表人",
        "fddbrzjlx":"法定代表人证件类型"
        "frzjhm":"法人证件号码"
        "tyshxydm" : "统一社会信用代码",
        "cflb1":"处罚类别1"
        "cflb2":"处罚类别2"
        "cfsy" : "处罚事由",
        "cfyj" : "处罚依据、
        "cfjg":"处罚结果",
        "zcxzcfjddwmc" : "作出行政处罚决定单位名称",
        "zcxzcfjdrq" : "作出行政处罚决定日期",
        "zzjgdm" : "组织机构代码",
        "gsdjh" : "工商登记码",
        "swdjh" : "税务登记号",
        "xzxdrmc" : "行政相对人名称",
        "wfxwdjrq":"违法行为登记日期",
        "cfjdszzrq":"处罚决定书制作日期",
        "cfsxq" : "处罚生效期",
        "cfjzq" : "处罚截止期",
        "dqzt" : "当前状态",
        "nsrzt"："纳税人状态"
        "province" : "省份",
        "city" : "城市",
        "dfbh": "地方编号",
        "bz":"备注"
        "gsqx":"公示期限"
        "fbjg":"发布机构"
        "fbsj":"发布时间"
        "fingerPrint":"指纹 //用于主键存储，去除重复记录"}
        ]
    }

#非正常户
"ENTNAME" : "纳税人名称"
fzch:{
    "operation":"append",
    "data_type":"sw",
    "data":[{
        "rowkeySource":"rowkey来源",# 非正常认定日期+纳税人识别号+纳税人名称+欠税金额+法定代表人身份证号码+当前新发生的欠税金额"
        "rowkey":"md5", 
        "zggsjg" : "主管国税机关",
        "nsrsbh" : "纳税人识别号",
        "nsrmc" : "纳税人名称",
        "fddbr" : "法定代表人",
        "fddbrzjlx":"法定代表人证件类型"
        "fddbrsfzhm" : "法定代表人身份证号码",
        "dom" : "生产经营地址",
        "fzcrdrq" : "非正常认定日期",
        "djzclx":"登记注册类型",
        "zzjgdm":"组织机构代码",
        "qsbz" : "欠税币种",
        "qssz":"欠税税种"
        "dqxfsdqsje":"当前新发生的欠税金额",
        "kprq":"开票日期",
        "jkqx":"缴款期限",
        "qsje" : "欠税金额",
        "province" : "省份",
        "city" : "城市",
        "bz":"备注",
        "fbjg":"发布机构",
        "fbsj":"发布时间",
        "fingerPrint":"指纹 //用于主键存储，去除重复记录",
        }
        ]
    }



