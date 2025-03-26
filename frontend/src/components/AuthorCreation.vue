<template>
    <v-container>
        <v-form @submit.prevent="createAuthor">
            <v-text-field v-model="authorName" label="Author name" required></v-text-field>
            <v-btn class="mt-2" color="primary" type="submit" block>Create Author</v-btn>
        </v-form>
    </v-container>
</template>

<script>
export default {
    data() {
        return {
            authorName: "",
        };
    },
    methods: {
        async createAuthor() {
            if (this.authorName) {
                const authorData = {
                    name: this.authorName,
                };
                try {
                    const response = await fetch(
                        'http://localhost:4000/authors', {
                            method: "POST",
                            headers: {
                                "Content-Type": "application/json",
                            },
                            body: JSON.stringify(authorData),
                        }
                    );
                    if (!response.ok) throw new Error("Failed to create author");
                    await response.json();
                    this.authorName = "";
                } catch (error) {
                    console.error("Error:", error);
                }
            }
        }
    },
};
</script>