import com.github.redouane59.twitter.TwitterClient;
import com.github.redouane59.twitter.dto.tweet.TweetV2;
import com.github.redouane59.twitter.dto.tweet.TweetV2.TweetData;
import com.github.redouane59.twitter.dto.user.UserV2;
import java.time.format.DateTimeFormatter;
import java.util.ArrayList;
import java.util.List;

public class TwitterETL {

    public static void main(String[] args) {
        // Replace with your actual Bearer Token
        String bearerToken = "AAAAAAAAAAAAAAAAAAAAAP%2BqzwEAAAAAnMPWANQk4k%2FZW6dOaGfRuV9eFZ8%3DQ1H5wEMNBeL7QVagx0keUG3pVbsxZFgLnQUBelpfeCpwNTlCis";

        // Initialize Twitter Client
        TwitterClient twitterClient = new TwitterClient(TwitterClient.OBJECT_MAPPER, bearerToken);

        // Get user information
        String username = "fisherwayy";
        UserV2 user = twitterClient.getUserFromUsername(username);
        if (user == null || user.getId() == null) {
            System.out.println("❌ User not found!");
            return;
        }
        String userId = user.getId();

        // Fetch tweets
        List<TweetData> tweets = twitterClient.getUserTimeline(userId, 100);
        if (tweets.isEmpty()) {
            System.out.println("No tweets found.");
            return;
        }

        // Process tweets
        List<String> tweetData = new ArrayList<>();
        DateTimeFormatter formatter = DateTimeFormatter.ofPattern("yyyy-MM-dd HH:mm:ss");

        for (TweetData tweet : tweets) {
            String formattedTweet = String.format(
                "User: %s | Text: %s | Likes: %d | Retweets: %d | Created At: %s",
                username,
                tweet.getText(),
                tweet.getPublicMetrics().getLikeCount(),
                tweet.getPublicMetrics().getRetweetCount(),
                tweet.getCreatedAt().format(formatter)
            );
            tweetData.add(formattedTweet);
        }

        // Print processed tweets
        tweetData.forEach(System.out::println);
    }
}
