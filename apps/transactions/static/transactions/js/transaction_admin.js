(function($) {
    $(document).ready(function() {
        function updateCategories(typeId) {
            var categorySelect = $('#id_category');
            categorySelect.prop('disabled', true);
            $.ajax({
                url: '/admin/transactions/category_by_type/', // Создадим этот урл
                data: { type: typeId },
                success: function(data) {
                    categorySelect.empty();
                    categorySelect.append($('<option></option>').attr('value', '').text('---------'));
                    $.each(data, function(idx, category) {
                        categorySelect.append($('<option></option>').attr('value', category.id).text(category.name));
                    });
                    categorySelect.prop('disabled', false);
                    categorySelect.trigger('change');
                }
            });
        }

        function updateSubcategories(categoryId) {
            var subcategorySelect = $('#id_subcategory');
            subcategorySelect.prop('disabled', true);
            $.ajax({
                url: '/admin/transactions/subcategory_by_category/', // Создадим этот урл
                data: { category: categoryId },
                success: function(data) {
                    subcategorySelect.empty();
                    subcategorySelect.append($('<option></option>').attr('value', '').text('---------'));
                    $.each(data, function(idx, subcategory) {
                        subcategorySelect.append($('<option></option>').attr('value', subcategory.id).text(subcategory.name));
                    });
                    subcategorySelect.prop('disabled', false);
                }
            });
        }

        $('#id_type').change(function() {
            var typeId = $(this).val();
            if(typeId) {
                updateCategories(typeId);
            } else {
                $('#id_category').empty().prop('disabled', true);
                $('#id_subcategory').empty().prop('disabled', true);
            }
        });

        $('#id_category').change(function() {
            var categoryId = $(this).val();
            if(categoryId) {
                updateSubcategories(categoryId);
            } else {
                $('#id_subcategory').empty().prop('disabled', true);
            }
        });

        // При загрузке страницы, если уже выбран type/category — обновим списки
        if($('#id_type').val()) {
            updateCategories($('#id_type').val());
        }
        if($('#id_category').val()) {
            updateSubcategories($('#id_category').val());
        }
    });
})(django.jQuery);
