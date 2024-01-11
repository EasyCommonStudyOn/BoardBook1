from .models import SubRubric


def bboard_context_processor(request):
    context = {}

    # Add all rubrics to the context
    context['rubrics'] = SubRubric.objects.all()

    # Initialize 'keyword' and 'all' in the context
    context['keyword'] = ''
    context['all'] = ' '

    # Check if 'keyword' is present in the GET parameters
    if 'keyword' in request.GET:
        keyword = request.GET['keyword']

        # Update 'keyword' in the context
        context['keyword'] = '?keyword=' + keyword

        # Update 'all' in the context
        context['all'] = context['keyword']

        # Check if 'page' is present in the GET parameters
        if 'page' in request.GET:
            page = request.GET['page']

            # Check if page is not 1 and update 'all' accordingly
            if page != '1':
                if context['all']:
                    context['all'] += '&page=' + page
                else:
                    context['all'] = '?page=' + page

    return context
