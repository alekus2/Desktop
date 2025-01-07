import os
import re
import csv
import datetime
from arcgis.gis import GIS
import pandas as pd

portalURL = r'https://gissp.bracell.com/portal/'
username = "Qualidade_SP"
password = "Qualidade@21"
survey_item_id = "35572da04c8f4193a518c888f20cda75"
save_path = r'F:\Qualidade_Florestal\02- MATO GROSSO DO SUL\11- Administrativo Qualidade MS\00- Colaboradores\17 - Alex Vinicius\Pasta de controle de mudas laudo'
keep_org_item = False
store_csv_w_attachments = True

gis = GIS(portalURL, username, password)
survey_by_id = gis.content.get(survey_item_id)

rel_fs = survey_by_id.read_excel('Survey2Service', 'forward')[0]
item_excel = rel_fs.export(title=survey_by_id, export_format='Excel')
item_excel.download(save_path=save_path)
if not bool(keep_org_item):
    item_excel.delete(force=True)

url_base_survey = r'F:"F:\Qualidade_Florestal\02- MATO GROSSO DO SUL\11- Administrativo Qualidade MS\00- Colaboradores\17 - Alex Vinicius\Pasta de controle de mudas laudo\QLD_laudo_de_qualidade_de_mudas_em_expedicao.xlsx"'
base_survey = pd.read_excel(url_base_survey)

layers = rel_fs.layers + rel_fs.tables

for i in layers:
    if i.properties.hasAttachments == True:
        csv_file_name = "{}_attachments.csv".format(re.sub(r'[^A-Za-z0-9]+', '', i.properties.name))
        path = os.path.join(save_path, csv_file_name)
        csv_fields = ['Parent objectId', 'Attachment path']
        with open(path, 'w', newline='') as csvfile:
            csvwriter = csv.writer(csvfile)
            csvwriter.writerow(csv_fields)
            feature_object_ids = i.query(where="1=1", return_ids_only=True, order_by_fields='objectid ASC')
            for j in range(len(feature_object_ids['objectIds'])):
                current_oid = feature_object_ids['objectIds'][j]
                current_oid_attachments = i.attachments.get_list(oid=current_oid)
                if len(current_oid_attachments) > 0:
                    for k in range(len(current_oid_attachments)):
                        attachment_id = current_oid_attachments[k]['id']
                        current_attachment_path = i.attachments.download(oid=current_oid, attachment_id=attachment_id, save_path=save_path)
                        csvwriter.writerow([current_oid, os.path.join(save_path, os.path.split(current_attachment_path[0])[1])])