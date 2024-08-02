import requests
import bs4
def links(InputLink):
    rq=requests.get(InputLink)
    bee=bs4.BeautifulSoup(rq.content,'html.parser')
    fa=str(bee.find_all('div',class_='max-height max-height-md-0 max-height-xs-400'))
    bee2=bs4.BeautifulSoup(fa,'html.parser')
    fam=bee2.find_all('a')
    links=[]
    for ob in fam:
        rob=str(ob)
        if rob[3]=='h':
            roo=rob.split('"')[1]
            links.append(roo)
        pass
    pass
    return(links)
pass
class AreaContent():
    def __init__(self, InputLink: str):
        rqac=requests.get(InputLink)
        beeac=bs4.BeautifulSoup(rqac.content,'html.parser')
        #Description
        debac=beeac.find('div', class_='fr-view')
        cra=str(debac).replace('<p>','\n').split('<')
        de=[]
        for ob in cra:
            if '>' in ob:
                obs=ob.split('>')[1]
                de.append(obs)
        pass
        self.Description=''.join(de)
        #Name
        nabrc=str(beeac.find('h1'))
        self.Name=nabrc.replace('\n','')[12:][::-1][288:][::-1]
class RouteContent():
    def Grade(InputLink: str):
            rqe=requests.get(InputLink)
            beerc=bs4.BeautifulSoup(rqe.content,'html.parser')
            grbrc=beerc.find('span',class_='rateYDS')
            return(str(grbrc).split('>')[1].split('<')[0].replace(' ',''))
    def Type(InputLink: str):
            rqe=requests.get(InputLink)
            beerc=bs4.BeautifulSoup(rqe.content,'html.parser')
            rtab=bs4.BeautifulSoup(str(beerc.find('table',class_='description-details')),'html.parser')
            tybrc=str(rtab.find_all('td')[1]).replace('\n','')
            return(tybrc.replace(' ','').split('>')[1].split('<')[0])
    def Stars(InputLink: str):
            rid=InputLink.split('/')[4]
            rqe=requests.get(InputLink)
            beerc=bs4.BeautifulSoup(rqe.content,'html.parser')
            stbrc=beerc.find('span',id=f'starsWithAvgText-{rid}')
            return(str(stbrc).split('</span>')[1].replace('\n','').split(' ')[5])
    def FA(InputLink: str):
            rqe=requests.get(InputLink)
            beerc=bs4.BeautifulSoup(rqe.content,'html.parser')
            rtab=bs4.BeautifulSoup(str(beerc.find('table',class_='description-details')),'html.parser')
            fabrc=str(rtab.find_all('td')[3])
            return(fabrc.replace('\n','')[44:][::-1][41:][::-1])
    def PageViews(InputLink: str):
            rqe=requests.get(InputLink)
            beerc=bs4.BeautifulSoup(rqe.content,'html.parser')
            rtab=bs4.BeautifulSoup(str(beerc.find('table',class_='description-details')),'html.parser')
            pvbrc=str(rtab.find_all('td')[5])
            return(int(pvbrc.replace('\n','')[4:].replace(' ','').split('t')[0].replace(',','')))
    def SharedBy(InputLink: str):
            rqe=requests.get(InputLink)
            beerc=bs4.BeautifulSoup(rqe.content,'html.parser')
            rtab=bs4.BeautifulSoup(str(beerc.find('table',class_='description-details')),'html.parser')
            sbbrc=str(rtab.find_all('td')[7])
            return(sbbrc.replace('\n','').split('>')[2].split('<')[0])
    def Name(InputLink: str):
            rqe=requests.get(InputLink)
            beerc=bs4.BeautifulSoup(rqe.content,'html.parser')
            nabrc=str(beerc.find('h1'))
            return(nabrc.replace('\n','')[12:][::-1][288:][::-1])
    def Area(InputLink: str):
            rqe=requests.get(InputLink)
            beerc=bs4.BeautifulSoup(rqe.content,'html.parser')
            lin=str(beerc.find('div',class_='mb-half small text-warm'))
            belin=bs4.BeautifulSoup(lin,'html.parser')
            lin2=list(belin.find_all('a'))
            rear=[]
            for line1 in lin2:
                rlin=str(line1)
                href=rlin.split('"')[1]
                rear.append(href)
            pass
            return(rear)
    def Pictures(InputLink: str):
            rqe=requests.get(InputLink)
            beerc=bs4.BeautifulSoup(rqe.content,'html.parser')
            pibrc=beerc.find_all('img',class_='lazy')
            image=[]
            for img in pibrc:
                we=str(img)
                if 'src=' in we:
                    im=we.split('src=')[1].split('"')[1]
                    image.append(im)
                pass
            pass
            return(image)
    def Description(InputLink: str):
            rqe=requests.get(InputLink)
            beerc=bs4.BeautifulSoup(rqe.content,'html.parser')
            debrc=beerc.find('div', class_='fr-view')
            cra=str(debrc).replace('<p>','\n').split('<')
            de=[]
            for ob in cra:
                if '>' in ob:
                    obs=ob.split('>')[1]
                    de.append(obs)
            pass
            return(''.join(de))
    pass
    pass
pass
class AllInfo():
      def __init__(self,InputLink: str):
            rqe=requests.get(InputLink)
            beerc=bs4.BeautifulSoup(rqe.content,'html.parser')
            grbrc=beerc.find('span',class_='rateYDS')
            rid=InputLink.split('/')[4]
            rtab=bs4.BeautifulSoup(str(beerc.find('table',class_='description-details')),'html.parser')
            self.Grade=str(grbrc).split('>')[1].split('<')[0].replace(' ','')

            tybrc=str(rtab.find_all('td')[1]).replace('\n','')
            self.Type=tybrc.replace(' ','').split('>')[1].split('<')[0].replace('\n','')
            

            stbrc=beerc.find('span',id=f'starsWithAvgText-{rid}')
            self.Stars=str(stbrc).split('</span>')[1].replace('\n','').split(' ')[5]

            fabrc=str(rtab.find_all('td')[3])
            self.FA=fabrc.replace('\n','')[44:][::-1][41:][::-1]

            pvbrc=str(rtab.find_all('td')[5])
            self.PageViews=(int(pvbrc.replace('\n','')[4:].replace(' ','').split('t')[0].replace(',','')))

            sbbrc=str(rtab.find_all('td')[7])
            self.SharedBy=(sbbrc.replace('\n','').split('>')[2].split('<')[0])

            nabrc=str(beerc.find('h1'))
            self.Name=nabrc.replace('\n','')[12:][::-1][288:][::-1]

            lin=str(beerc.find('div',class_='mb-half small text-warm'))
            belin=bs4.BeautifulSoup(lin,'html.parser')
            lin2=list(belin.find_all('a'))
            rear=[]
            for line1 in lin2:
                rlin=str(line1)
                href=rlin.split('"')[1]
                rear.append(href)
            pass
            self.Area=(rear)


            pibrc=beerc.find_all('img',class_='lazy')
            image=[]
            for img in pibrc:
                we=str(img)
                if 'src=' in we:
                    im=we.split('src=')[1].split('"')[1]
                    image.append(im)
                pass
            pass
            self.Pictures=(image)

            debrc=beerc.find('div', class_='fr-view')
            cra=str(debrc)[4:].replace('<p>','\n').split('<')
            de=[]
            for ob in cra:
                if '>' in ob:
                    obs=ob.split('>')[1]
                    de.append(obs)
            pass
            self.Description=(''.join(de))
            pass
pass
pass
if __name__=='__main__':
    print(RouteContent.SharedBy('https://www.mountainproject.com/route/123999696/the-bloody-throne'))