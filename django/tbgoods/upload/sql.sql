select 
REPLACE(a.orderIds,',','|')as �������,
a.iiNumber as ��Ʊ���,
a.iiDate as ��Ʊ����,
a.outDate as ��Ʊʱ��,
(select m.miiName from crm_makeInvoiceInfo m where m.miiid=a.miiid) as ��Ʊ��λ,
(e.mc + e.mxSpec) as ��ƱƷ��,
d.ilQuantity as ��Ʊ����,
d.salePrice as ���ۼ۸�,
d.ilPrice as ��Ʊ����,
d.taxrate as ˰��,
d.taxCost as ˰��,
(d.sub_total) as ��Ʊ���,
d.ilItype as [��Ʊ����(1-��Ʊ/2-��ֵƱ)],
a.iiCheck as ���,
a.iiDone as ��ɱ�־,
b.khmc as �ͻ�����,
c.ygxm as ҵ����Ա 
from oa_crm_invoice_info a,oa_crm_khxx b,rs_ygb c,oa_crm_invoice_list d,oa_crm_dzcpfwxx e 
where a.khbh=b.khbh and a.iiMan=c.ygbh and a.iiid=d.iiid and d.cpbh=e.cpbh  
Order by a.iiDate desc


