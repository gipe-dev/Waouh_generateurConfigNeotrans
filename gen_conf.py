import os
import xml
from shutil import copyfile
import re

conf_1: list = ['142A', '161A', '162A', '163A', '164A', '168D', '194A', '195A', '196A', '197A', '198A', "199A", "200A",
                '139A', '140A']
conf_2: list = [
    '05D', '74D', '96D', '121D',
    '08D', '76D', '100D', '122D',
    '10D', '77D', '101D', '123D', '145D',
    '19D', '78D', '103D', '124D', '146D',
    '20D', '79D', '104D', '125D', '147D',
    '23D', '80D', '106D', '126D', '148D',
    '31D', '81D', '107D', '127D', '149D',
    '32D', '83D', '109D', '128D', '150D',
    '39D', '84D', '110D', '111D', '129D', '151D',
    '64D', '85D', '112D', '130D', '174D',
    '66D', '86D', '113D', '131D', '188D',
    '67D', '87D', '114D', '132D', '189D',
    '68D', '88D', '115D', '133D', '190D',
    '69D', '91D', '116D', '134D', '191D',
    '70D', '92D', '117D', '135D', '192D',
    '71D', '93D', '118D', '136D', '193D',
    '72D', '94D', '119D', '137D',
    '73D', '95D', '120D', '138D',
]
conf_2_hyb: list = ['12D', '21D', '30D', '35D', '143D', '165D', '179D']
conf_3: list = ['141A', '144A', '166A', '178A', '176A']
conf_4: list = ['43D', '44D', '45D', '46D', '47D', '48D', '49D', '50D', '51D', '52D', '53D', '54D', '55D', '56D',
                '57D', '58D', '59D', '62D', '63D']

conf_sim: list = ['60B', '61B']
conf_1_lc: list = ['02A', '07A', '13A', '14A', '15A', '16A', '17A', '24A', '25A', '29A', '34A', '36A', '38A', '41A',
                   '42A', '152A', '153A', '154A', '156A', '157A', '158A', '161A', '167A', '170A', '171A', '172A']
conf_2_lc: list = ['1A', '3A', '6A', '33A', '37A', '40A', '155A', '159A', '160A', '169A', '173A', '175A', '177A',
                   '180A', '181A', '182A', '183A', '184A', '185A', '186A', '187A']

all_conf: list = ['conf_1', 'conf_2', 'conf_2_hyb', 'conf_3', 'conf_4', 'conf_1_lc', 'conf_2_lc', 'conf_sim']

tmpl_path: str = "\\Rame_tmpl.xml"
out_path = ".\\output"

os.makedirs(out_path, exist_ok=True)

verDR: str = "1.16"
verPE: str = "1.14"
verC: str = "1.15"
pld_kern_version: str = "3.2.1.0"
pld_app_version: str = "1.9.2.2"
pld_media_content_version: str = "1.14.0.25_DR"
led_kern_version: str = "3.2.0.1"
led_app_version: str = "1.9.2.2"

ligne_versions = {
    'ligne_D_R': {"ver": verDR,
                  "pld_kern_version": pld_kern_version,
                  "pld_app_version": pld_app_version,
                  "led_kern_version": led_kern_version,
                  "led_app_version": led_app_version,
                  "pld_media_content_version": "1.16.0.0_ligneDR",
                  "led_media_content_version": "1.16.0.0_ligneDR"
                  },
    'ligne_P_E': {"ver": verPE,
                  "pld_kern_version": pld_kern_version,
                  "pld_app_version": pld_app_version,
                  "led_kern_version": led_kern_version,
                  "led_app_version": led_app_version,
                  "pld_media_content_version": "1.14.3.0_EP",
                  "led_media_content_version": "1.14.3.0_EP"
                  },
    'ligne_C': {"ver": verC,
                "pld_kern_version": pld_kern_version,
                "pld_app_version": pld_app_version,
                "led_kern_version": led_kern_version,
                "led_app_version": led_app_version,
                "pld_media_content_version": "1.15.0.2_ligneC",     # = data in manifest.xml
                "led_media_content_version": "1.15.0.2_ligneC"
                },
}


def replace_in_file(file_path: str, number: str, train_line: str):
    with open(file_path, 'r+') as f:
        text = f.read()
        text = re.sub('##ver##', ligne_versions[train_line]["ver"], text)
        text = re.sub('##rame_num##', number, text)
        text = re.sub('##pld_kern_version##', ligne_versions[train_line]["pld_kern_version"], text)
        text = re.sub('##pld_app_version##', ligne_versions[train_line]["pld_app_version"], text)
        text = re.sub('##pld_media_content_version##', ligne_versions[train_line]["pld_media_content_version"], text)
        text = re.sub('##led_kern_version##', ligne_versions[train_line]["led_kern_version"], text)
        text = re.sub('##led_app_version##', ligne_versions[train_line]["led_app_version"], text)
        text = re.sub('##led_media_content_version##', ligne_versions[train_line]["led_media_content_version"], text)
        text = re.sub('##IP_RAME##', number[:-1], text)
        f.seek(0)
        f.write(text)
        f.truncate()


if __name__ == '__main__':
    all_var: dict = globals()

    for key_line, _ in ligne_versions.items():
        for conf in all_conf:
            for rame_num in all_var[conf]:
                src = f".\\Rames Waouh\\" + conf + tmpl_path
                path = f"{out_path}\\{key_line}\\"
                dst = f"{path}{rame_num}.xml"
                os.makedirs(path, exist_ok=True)
                copyfile(src, dst)
                replace_in_file(dst, rame_num, key_line)
    pass
