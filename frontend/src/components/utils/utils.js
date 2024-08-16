import { useRouter } from 'vue-router';

export function generateTargetUrl(buttonName) {
  const router = useRouter();
  const currentQueryParams = router.currentRoute.value.query;

  if (Object.keys(currentQueryParams).length === 0) {
    return `?utm_source=jobs_yourcodereview&utm_term=${buttonName || ''}`;
  } else if (currentQueryParams.utm_term !== undefined){
    currentQueryParams.utm_term = buttonName || '';
    return `?${new URLSearchParams(currentQueryParams)}`;
  } else {
    return `?${new URLSearchParams(currentQueryParams)}&utm_term=${buttonName || ''}`;
  }
}
