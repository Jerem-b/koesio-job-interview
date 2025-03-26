<template>
    <v-container>
        <v-form @submit.prevent="updateAuthor">
            <v-text-field v-model="author.name" label="Author Name" required></v-text-field>

            <v-btn type="submit" color="primary" class="mt-3">Update Author</v-btn>
        </v-form>
        <v-divider></v-divider>
        <BooksByAuthor :authorName="author.name" />
    </v-container>
</template>

<script>
import BooksByAuthor from '../components/BooksByAuthor.vue';

export default {
    components: {
        BooksByAuthor,
    },
    data() {
        return {
            author: {
                name: '',
                books: [],
            },
        };
    },
    created() {
        this.fetchAuthor();
    },
    methods: {
        async fetchAuthor() {
            const authorId = this.$route.params.id;
            try {
                const response = await fetch(`http://localhost:4000/authors/${authorId}`);
                const data = await response.json();
                this.author = data.author;
            } catch (error) {
                console.error('Error fetching author:', error);
            }
        },
        async updateAuthor() {
            const authorId = this.$route.params.id;
            try {
                const response = await fetch(`http://localhost:4000/authors/${authorId}`, {
                    method: 'PATCH',
                    headers: {
                        'Content-Type': 'application/json',
                    },
                    body: JSON.stringify({
                        'name': this.author.name,
                    }),
                });

                if (response.ok) {
                    this.$router.push('/authors');
                } else {
                    console.error('Failed to update author');
                }
            } catch (error) {
                console.error('Error updating author:', error);
            }
        },
    },
};
</script>