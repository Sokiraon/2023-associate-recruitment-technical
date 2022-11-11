select owner.owner_id, owner.owner_name, unique(category.category_id) as diversity
from owner, article, category_article_mapping mapping, category
order by diversity desc
where owner.owner_id == article.owner_id
and article.article_id == mapping.article_id
and mapping.category_id == category.category_id;