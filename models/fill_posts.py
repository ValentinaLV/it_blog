from app import db
from models.post import Post
from models.tag import Tag


# -----Post db insert-----
db.create_all()
# Post.query.filter(Post.id == 17).delete()
# Post.query.filter(Post.id == 19).delete()
# Post.query.filter(Post.id == 20).delete()
# db.session.commit()
posts = Post.query.all()
print(posts)
p1 = Post(title='7 Skills to Help You Get Noticed by Hiring Companies in 2020',
         body='Need a leg up on the competition finding your first or next position this upcoming year? '
              'Be warned: the top professional skills desired these days are less science- and '
              'tech-oriented, and more liberal arts-oriented. With AI and machine learning becoming '
              'a big part of the work-life along with social media and the likes taking over the personal, '
              'employers note a lack of interpersonal and humanity-based professional skills they find '
              'mperative in today’s job market. Hence, the shift from the highly technical skills to the '
              'more flexible one. 7 Most Helpfully Skills: Visualizing Data, Creativity, Emotional Intelligence,'
              'Complex Problem-Solving, Cognitive Flexibility, People Management, Negotiation. '
              'Learn more on www.simplilearn.com')
p2 = Post(title='Top Business and IT Certification Courses for 2020',
          body='If your career has been built upon technologies or practices that are fading away, '
               'it’s time to get reskilled and ready for your next opportunity. Below are '
               '11 business and IT career fields offering numerous potential job opportunities '
               'and the certifications that can help you to jumpstart or jump ahead in those fields: '
               'Artificial Intelligence and Machine Learning, Big Data, Data Science, Cloud Computing, '
               'Project Management, Business Intelligence, Networking, Software Development, DevOps, '
               'Cyber Security, Digital Marketing. '
               'Learn more on www.simplilearn.com')
p3 = Post(title='Top 10 Highest Paying Tech Jobs in 2020',
          body='We live in a time of great change career-wise; jobs are lost to automation and others are '
               'changing what skills are required. With changes like these in the market, '
               'you may be considering a shift to a career in technology or, perhaps, you’re '
               'already in the field and want to advance. Whatever your reason, we’ve pulled together a '
               'list of the 10 highest paying tech jobs in 2020 for you. Top 10 Highest Paying Tech Jobs: '
               '10: Product Manager, 9: Full Stack Developer, 8: Cloud Architect, 7: Artificial Intelligence (AI) Engineer, '
               '6: DevOps Engineer, 5: Blockchain Engineer, 4: Software Architect, 3: Internet of Things (IoT) Solutions Architect, '
               '2: Big Data Engineer, 1: Data Scientist. '
               'Learn more on www.simplilearn.com')
p4 = Post(title='Top 8 Technology Trends for 2020',
          body='Technology is now evolving at such a rapid pace that annual predictions of '
               'trends can seem out-of-date before they even go live as a published blog post '
               'or article. As technology evolves, it enables even faster change and progress, '
               'causing an acceleration of the rate of change, until eventually it will become '
               'exponential. So there are 8 main technologies trends in 2020: Artificial Intelligence (AI), '
               'Machine Learning, Robotic Process Automation or RPA, Edge Computing, Virtual Reality and Augmented Reality, '
               'Blockchain, Internet of Things (IoT), Cybersecurity. '
               'Learn more on www.simplilearn.com')
# db.session.add_all([p1, p2, p3, p4])
# db.session.commit()
# print(p1.slug)
# print(p2.slug)
# print(p3.slug)
# print(p4.slug)
# posts = Post.query.all()
# print(posts)

p5 = Post(title='Is Your Health Data at Risk?',
          body='It utilizes Linux Mint\'s Cinnamon desktop environment on top of Ubuntu Linux\'s codebase. '
               'Work on several release candidate and beta versions stretches back to 2013. The efforts'
               'stayed under the radar until the announcement of the new distro\'s debut stable release.')

p6 = Post(title='China\'s Tech Ban Could Have Grave Long-Term Consequences',
          body='China has issued an order that all foreign-made computer equipment and software be removed '
               'from government offices and public institutions within the next three years.'
               'The news of Beijing\'s move came earlier this week in a report from the Nikkei-owned, '
               'London-based Financial Times. China has estimated that upwards of 30 million pieces of hardware '
               'will need to be replaced, the paper noted.')

db.session.add_all([p5, p6])
db.session.commit()


