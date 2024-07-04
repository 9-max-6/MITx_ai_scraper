import getpass
import os

os.environ["OPENAI_API_KEY"] = getpass.getpass()

from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser 
from langchain_core.prompts import ChatPromptTemplate

model = ChatOpenAI(model="gpt-4")
parser = StrOutputParser()

system_template = """Extract the information included in the structure below 
    from the given html content extracted from a website. The structure is as follows:
            <intro>: Introduction to the opportunity,
            <main>: Main content of the opportunity,
            <conclusion>: The conclusion of the opportunity,
            <procedure>: Any relevant information about the opportunitys application procedures,
            <size>: The size of the opportunity in dollars,
            <rel_score>: Relevance of the opportunity. For now just give 1 for each,
            <deadline>: Deadline to application of opportunity in the format YYYY-MM-DD e.g 2022-12-12,
            <summary>: A summary of the opportunity
            <org>: The organization offering the opportunity,
            country: The country that has posted the tender,
            date_published: The date that the opportunity was published according in the format YYYY-MM-DD e.g 2022-12-12
         
        The opportunity is to be formatted in JSON format with no other accompanying text. such as the structure show below:
            "intro": "Introduction to the opportunity",
            "main": "Main content of the opportunity",
            "conclusion": "The conclusion of the opportunity",
            "procedure": "Any relevant information about the opportunitys procedure",
            "size": "10000",
            "rel_score": "0.5",
            "ref_number": "1234",
            "deadline": "2022-12-12",
            "summary": "A summary of the opportunity",
            "org": "The organization offering the opportunity",
            "country": "Burundi",
            "date_published": "2022-12-12"'"""

html_content = """<p><b>SELECTION OF CONSULTING FIRMS BY THE WORLD BANK GROUP 
    </b></p><p><b>REQUEST FOR EXPRESSION OF INTEREST (EOI)</b></p><p>Electronic 
        Submissions through <a href="https://wbgeprocure-rfxnow.worldbank.org/rfxnow" 
            rel="nofollow">WBGeProcure RFx Now</a></p><p><b>ASSIGNMENT OVERVIEW</b></p><p> 
                Assignment Title: Independent Evaluation of Human Rights Inclusion and 
                    Empowerment Trust Fund </p><p>Assignment Countries: </p><p>- Not Country 
                        Related</p><p><b>ASSIGNMENT DESCRIPTION</b></p><p></p><p>The World Bank 
                            is seeking the services of an experiencedrnconsulting firm 
                                to prepare and deliver an independent evaluation of the HumanrnRights, 
                                    Inclusion and Empowerment (HRIE) Umbrella Trust Fund.  
                                    The objectives for this independentrnevaluation include: 
                                        (a) assess the efficiency and effectiveness of 
                                            thernfinancial and technical inputs provided by the HRIE in generating 
                                                results at HQrnand country levels and how it can be strengthened in the future; 
                                                (b) assess thernsustainability of the HRIEs outcomes, and in particular 
                                                    institutionalrnsustainability, and how it can be strengthened in the future; 
                                                    (c) identifyrninternal and external factors contributing to the ability of the HRIE tornfulfill its mandate; and, (d) identify good practices 
                                                        and lessons learned andrnexplore options for a 
                                                            future trust fund phase. </p><p>The evaluation has a dual purpose of assessing results ex-post 
                                                            andrnproviding recommendations for continuation of the Umbrella.  The evaluation also seeks the evaluators to providernrecommendations 
                                                                for consideration and action by development partners andrndecision-makers 
                                                                    and stakeholders in the World Bank, especially related 
                                                                    to thernfuture of the trust fund. </p><p>This evaluation will be guided by the criteria 
                                                                        (relevance,rneffectiveness, efficiency, impact, and sustainability) as laid out in the 2018 OECDrnDAC Criteria for Evaluating Development Assistance,<a href="https://worldbankgroup-my.sharepoint.com/personal/aeftimiadis_worldbankgroup_org/Documents/LDriveWBG/1%20Social%20GLU/HRDTF/Evaluation/Advertisement%20text.docx#_ftn1" rel="nofollow"><sup><sup><span style="font-size:11pt;line-height:107%;font-family:&#39;calibri&#39; , sans-serif">[1]</span></sup></sup></a><sup>rn</sup> and will also incorporate elementsrnfrom the Norms and Standards for Evaluation of the UN System on IntegratingrnHuman Rights and Gender Equality in Evaluation.  The application of the criteria should bernconsistent with the summative nature of the evaluation and the operationalrnmodel of HRIE within the Banks Social Inclusion Global Practice. Thernevaluators are encouraged to further develop and refine the guiding questionsrnpresented below under each criterion and to include additional questions theyrnmay deem important.</p><p style="margin-bottom:0in;margin-bottom:0in;margin-top:0in;text-align:justify;line-height:normal">Thernevaluators should propose the appropriate methodology – reflecting bothrnperformance and process evaluation, as well as recommendations for futurernimprovements. The evaluation should be conducted based on key evaluationrnquestions, which may include key informant interviews, desk review of corernactivity documentation (proposal summary forms, project and program progressrnreports, program annual reports, Partnership Council (governing body) meetingrnminutes, program charter, secondary data sources, etc.).  </p><p style="margin-bottom:0in;margin-bottom:0in;margin-top:0in;text-align:justify;line-height:normal"> </p><p>rnrnrnrnrnrnrnrnrnrn</p><div>rnrnrnrn<div>rnrn<p><a href="https://worldbankgroup-my.sharepoint.com/personal/aeftimiadis_worldbankgroup_org/Documents/LDriveWBG/1%20Social%20GLU/HRDTF/Evaluation/Advertisement%20text.docx#_ftnref1" rel="nofollow"><i><span style="font-size:10pt;line-height:107%;font-family:&#39;calibri&#39; , sans-serif"><b><span style="font-size:10pt;line-height:107%">[1]</span></b></span></i></a><i><span 
                                            style="font-size:10pt;line-height:107%"> Throughout their appraisal of the HRIE,rnevaluators 
                                                should emphasize </span></i><i><span style="font-size:10pt;l 
                                                ine-height:107%">five criteria, commonly referred to as the 2018 OECD </span></i><i><span style="font-size:10pt;line-height:107%"><a href="https://www.oecd.org/dac/evaluation/2754804.pdf" rel="nofollow">DAC criteria</a></span></i><i><span style="font-size:10pt;line-height:107%">, </span></i><i><span style="font-size:10pt;line-height:107%">most widely used tornevaluate development interventions—i.e. relevance, efficiency, effectiveness,rnimpact and sustainability.  In addition,rnthe evaluators should refer to the </span></i><i><span style="font-size:10pt;line-height:107%"><a href="http://www.unevaluation.org/document/detail/1914" rel="nofollow"><span style="color:rgb( 0 , 108 , 183 )">Norms and Standards for Evaluation in the UN System</span></a></span></i><i><span style="font-size:10pt;line-height:107%;color:rgb( 69 , 69 , 69 )">, </span></i><i><span style="font-size:10pt;line-height:107%"><a href="http://www.uneval.org/document/download/2107" rel="nofollow"><span style="color:rgb( 0 , 108 , 183 )">UNEGrnGuidance on Integrating Human Rights and Gender Equality in Evaluation,</span></a>rnto ensure the incorporation of a human rights lens.  </span></i><i><span style="font-size:10pt;line-height:107%"></span></i></p>rnrn</div>rnrn</div><p></p><p><b>FUNDING SOURCE</b></p><p>The World Bank Group intends to finance the assignment / services described below under the following:</p><ul><li>TF073224: NTF</li></ul><p><b>ELIGIBILITY</b></p><p>Eligibility restrictions apply:</p><ul><li>[Please type list of restrictions]</li></ul><p><b>SUBMISSION REQUIREMENTS</b></p><p>The World Bank Group invites eligible firms to indicate their interest in providing the services.  Interested firms must provide information indicating that they are qualified to perform the services (brochures, description of similar assignments, experience in similar conditions, availability of appropriate skills among staff, etc. for firms; CV and cover letter for individuals).  Please note that the total size of all attachments should be less than 5MB.  Firms may associate to enhance their qualifications unless otherwise stated in the solicitation documents. Where a group of firms associate to submit an EOI, they must indicate which is the lead firm. If shortlisted, the firm identified in the EOI as the lead firm will be invited to the request for proposal (RFP) phase.</p><p>Expressions of Interest should be submitted, in English, electronically through <a href="https://wbgeprocure-rfxnow.worldbank.org/rfxnow" rel="nofollow">WBGeProcure RFx Now</a></p><p><b>NOTES</b></p><p>Following this invitation for EOI, a shortlist of qualified firms will be formally invited to submit proposals. Shortlisting and selection will be subject to the availability of funding.</p><p>Only those firms which have been shortlisted will be invited to participate in the RFP phase. No notification or debrief will be provided to firms which have not been shortlisted.</p><p>If you encounter technical difficulties while uploading documents, please send an e-mail to the Help Desk at 
                                                    <a href="corporateprocurement&#64;worldbank.org" rel="nofollow">corporateprocurement&#64;worldbank.org</a> prior to the submission deadline.</p>'
"""
 
prompt_template = ChatPromptTemplate.from_messages(
[("system", "{system_template}"), ("user", "{html_content}")]
)

chain = prompt_template | model | parser
result = chain.invoke({"html_content": html_content, "system_template": system_template})

print(result)
