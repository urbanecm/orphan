SELECT page.page_id, page.page_namespace, page.page_title, page.page_namespace Mod 2 AS Výraz1, page_1.page_title, page_1.page_id, page_1.page_namespace FROM page LEFT JOIN page AS page_1 ON (page.page_namespace = page_1.page_namespace+1) AND (page.page_title = page_1.page_title) WHERE page.page_namespace=1 AND ((page_1.page_title) Is Null));
