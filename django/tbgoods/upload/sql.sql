select 
REPLACE(a.orderIds,',','|')as 订单编号,
a.iiNumber as 开票编号,
a.iiDate as 开票日期,
a.outDate as 出票时间,
(select m.miiName from crm_makeInvoiceInfo m where m.miiid=a.miiid) as 开票单位,
(e.mc + e.mxSpec) as 开票品种,
d.ilQuantity as 开票数量,
d.salePrice as 销售价格,
d.ilPrice as 开票单价,
d.taxrate as 税率,
d.taxCost as 税金,
(d.sub_total) as 开票金额,
d.ilItype as [发票类型(1-普票/2-增值票)],
a.iiCheck as 审核,
a.iiDone as 完成标志,
b.khmc as 客户名称,
c.ygxm as 业务人员 
from oa_crm_invoice_info a,oa_crm_khxx b,rs_ygb c,oa_crm_invoice_list d,oa_crm_dzcpfwxx e 
where a.khbh=b.khbh and a.iiMan=c.ygbh and a.iiid=d.iiid and d.cpbh=e.cpbh  
Order by a.iiDate desc


